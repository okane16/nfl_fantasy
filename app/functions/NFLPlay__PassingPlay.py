
# Add your models & start the development server to import these types
from app.datamodels.NFL import NFLPlay, PassingPlay, NFLPlayDetails, NFLPlayer

from moose_lib import StreamingFunction, cli_log, CliLogData
from typing import Optional
from datetime import datetime

def get_team_info(source: NFLPlay) -> tuple[str, str, str, str, str, str, str]:
    if source.start_situation["possession"]["alias"] == source.home_team["alias"]:
        offensive_team_score = source.home_points
        offensive_team_alias = source.home_team["alias"]
        offensive_team = f"{source.home_team["market"]} {source.home_team["name"]}"
        defensive_team_score = source.away_points
        defensive_team_alias = source.away_team["alias"]
        defensive_team = f"{source.away_team["market"]} {source.away_team["name"]}"
    else:
        offensive_team_score = source.away_points
        offensive_team_alias = source.away_team["alias"]
        offensive_team = f"{source.away_team["market"]} {source.away_team["name"]}"
        defensive_team_score = source.home_points
        defensive_team_alias = source.home_team["alias"]
        defensive_team = f"{source.home_team["market"]} {source.home_team["name"]}"
    return offensive_team, offensive_team_alias, offensive_team_score, defensive_team, defensive_team_alias, defensive_team_score   


# def get_play_segment_yardage(start_location: NFLPlayLocation, end_location: NFLPlayLocation, offensive_team_alias: str) -> int:
#     start_yardline = start_location["yardline"]
#     end_yardline = end_location["yardline"]
#     if start_location["alias"] != offensive_team_alias:
#         start_yardline = 100 - start_yardline
#     if end_location["alias"] != offensive_team_alias:
#         end_yardline = 100 - end_yardline
#     return end_yardline - start_yardline


## MAIN FUNCTION ##
def fn(source: NFLPlay) -> Optional[PassingPlay]:
    if source.event_type != "pass":
        cli_log(CliLogData(action="No pass", message=f"Event Type: {source.event_type}", message_type="Info"))
        return None

    offensive_team, offensive_team_alias, offensive_team_score, defensive_team, defensive_team_alias, defensive_team_score = get_team_info(source)
    passer = receiver = ""
    tackler = hitter = None
    pass_result = ""
    first_down_converted = False
    pass_yards = 0
    pass_attempted_at_yardline = 0
    defensive_player_thrown_to = defensive_player_thrown_to_position = None
    interception_player = None
    first_down_converted = False

    for detail in source.details:
        category = detail.get("category")
        cli_log(CliLogData(action="Detail", message=f"detail: {category}", message_type="Info"))

        if category in {"pass", "pass_completion", "pass_interception"}:
            passer = detail["players"][0]
            pass_attempted_at_yardline = (
                detail["start_location"]["yardline"]
                if detail["start_location"]["alias"] == offensive_team_alias
                else 100 - detail["start_location"]["yardline"]
            )
            if category == "pass_interception":
                pass_result = "intercepted"
            if category == "pass_completion":
                pass_result = "completed"
            if category == "pass":
                pass_result = "incomplete"
                
            cli_log(CliLogData(action="Got passer", message=f"passer: {passer}", message_type="Info"))
            cli_log(CliLogData(action="Got Pass Attempt Yardline", message=f"pass_attempted_at_yardline: {pass_attempted_at_yardline}", message_type="Info"))
            cli_log(CliLogData(action="Got Pass Outcome", message=f"pass_result: {pass_result}", message_type="Info"))

        elif category in {"pass_reception", "pass_interception_return", "pass_incompletion"}:
            for player in detail["players"]:
                if player.get("role") == "return":
                    interception_player = player
                    cli_log(CliLogData(action="Got interception player", message=f"interception_player: {interception_player}", message_type="Info"))
                if player.get("role") in {"receive", "catch"}:
                    receiver = player
                    cli_log(CliLogData(action="Got receiver", message=f"receiver: {receiver}", message_type="Info"))
                if player.get("role") == "defend":
                    defensive_player_thrown_to = player
                    pass_result = "defended"
                    cli_log(CliLogData(action="Got defensive player thrown to", message=f"defensive_player_thrown_to: {defensive_player_thrown_to}", message_type="Info"))

            
            pass_caught_at_yardline = (
                detail["start_location"]["yardline"]
                if detail["start_location"]["alias"] == offensive_team_alias
                else 100 - detail["start_location"]["yardline"]
            )
            cli_log(CliLogData(action="Got Pass Caught Yardline", message=f"pass_caught_at_yardline: {pass_caught_at_yardline}", message_type="Info"))
            pass_yards = pass_caught_at_yardline - pass_attempted_at_yardline
            cli_log(CliLogData(action="Got Pass Yards", message=f"pass_yards: {pass_yards}", message_type="Info"))
            play_ended_at_yardline = (
                detail["end_location"]["yardline"]
                if detail["end_location"]["alias"] == offensive_team_alias
                else 100 - detail["end_location"]["yardline"]
            )
            cli_log(CliLogData(action="Got Play Ended Yardline", message=f"play_ended_at_yardline: {play_ended_at_yardline}", message_type="Info"))
            yards_after_catch = play_ended_at_yardline - pass_caught_at_yardline
            cli_log(CliLogData(action="Got Yards After Catch", message=f"yards_after_catch: {yards_after_catch}", message_type="Info"))
            net_play_yards = pass_yards + yards_after_catch
            cli_log(CliLogData(action="Got Net Play Yards", message=f"net_play_yards: {net_play_yards}", message_type="Info"))
            
        elif category == "sack":
            cli_log(CliLogData(action="Got Sack", message=f"sack: {detail}", message_type="Info"))
            outcome = "sack"
            sack_yards = detail.get("yards", 0)
            if detail.get("players"):
                tackler = detail["players"][0]
                cli_log(CliLogData(action="Got tackler", message=f"tackler: {tackler}", message_type="Info"))
            else:
                cli_log(CliLogData(action="No tackler", message=f"outcome: {detail.get('description', '')}", message_type="Info"))
                
        elif category == "tackle" or category == "pushed_out_of_bounds":
            if detail.get("players"):
                tackler = detail["players"][0]
                cli_log(CliLogData(action="Got tackler", message=f"tackler: {tackler}", message_type="Info"))
            else:
                cli_log(CliLogData(action="No tackler", message=f"outcome: {detail.get('description', '')}", message_type="Info"))
                
        elif category == "qb_hit":
            hitter = detail["players"][0]
            cli_log(CliLogData(action="Got hitter", message=f"hitter: {hitter}", message_type="Info"))
        elif category == "first_down":
            first_down_converted = True
            cli_log(CliLogData(action="Got first down", message=f"first_down_converted: {detail}", message_type="Info"))
        
    
    play = PassingPlay(  
        play_id=source.id,
        game_id=source.game_id,
        quarter=source.period["number"],
        clock_time=source.clock,
        offensive_team=offensive_team,
        offensive_team_alias=offensive_team_alias,
        offensive_team_score=offensive_team_score,
        defensive_team=defensive_team,
        defensive_team_alias=defensive_team_alias,
        defensive_team_score=defensive_team_score,
        start_yardline=source.start_situation["location"]["yardline"],
        end_yardline=source.end_situation["location"]["yardline"],
        start_down=source.start_situation["down"],
        yfd=source.start_situation["yfd"],
        first_down_converted=first_down_converted,
        passer=passer["name"],
        passer_position=passer["position"],
        pass_yards=pass_yards,
        pass_direction="",
        receiver=receiver["name"] if receiver else None,
        receiver_position=receiver["position"] if receiver else None,
        yards_after_catch=0,
        pass_result=pass_result,
        tackler=tackler["name"] if tackler else None,
        tackler_position=tackler["position"] if tackler else None,
        qb_hit=True if hitter else False,
        hitter=hitter["name"] if hitter else None,
        hitter_position=hitter["position"] if hitter else None,
        interception_player=interception_player["name"] if interception_player else None,
        interception_player_position=interception_player["position"] if interception_player else None,
        defensive_player_thrown_to=defensive_player_thrown_to,
        defensive_player_thrown_to_position=defensive_player_thrown_to_position,
    )
    return play

my_function = StreamingFunction(
    run=fn
)
