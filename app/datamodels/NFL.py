from dataclasses import dataclass
from moose_lib import Key, moose_data_model
from datetime import datetime
from typing import Optional

@moose_data_model
@dataclass
class PassingPlay:
    play_id: Key[str]
    game_id: Key[str]
    quarter: int
    clock_time: str
    offensive_team: str
    offensive_team_alias: str
    offensive_team_score: int
    defensive_team: str
    defensive_team_alias: str
    defensive_team_score: int
    start_yardline: int
    end_yardline: int
    start_down: int
    yfd: int
    first_down_converted: bool
    passer: str
    passer_position: str
    pass_yards: Optional[int]
    pass_direction: Optional[str]
    receiver: Optional[str]
    receiver_position: Optional[str]
    yards_after_catch: Optional[int]
    pass_result: str ## completed, intercepted, incomplete
    tackler: Optional[str]
    tackler_position: Optional[str]
    qb_hit: Optional[bool]
    hitter: Optional[str]
    hitter_position: Optional[str]
    interception_player: Optional[str]
    interception_player_position: Optional[str]
    defensive_player_thrown_to: Optional[str]
    defensive_player_thrown_to_position: Optional[str]
    

## ------------------TEAMS------------------##
@dataclass 
class NFLTeam:
    alias: str
    id: Key[str]
    sr_id: Key[str]
    market: str
    name: str
    used_timeouts: Optional[int]
    remaining_timeouts: Optional[int]
    used_challenges: Optional[int]
    remaining_challenges: Optional[int]
    points: Optional[int]

## ------------------GAME CONTEXT------------------##  
@dataclass
class NFLSeason:
    id: Key[str]
    year: int
    type: str
    name: str

@dataclass
class NFLWeek:
    id: Key[str]
    sequence: int
    title: str
    
@dataclass 
class NFLVenueLocation:
   latitude: Key[str]
   longitude: Key[str]
   

@dataclass
class NFLVenue:
    id: Key[str]
    name: str
    alias: str
    city: str
    state: str
    country: str
    zip: str
    address: str
    capacity: int
    surface: str
    roof_type: str
    sr_id: str
    location: NFLVenueLocation

# @dataclass
# class NFLGameSummary:
#     season: NFLSeason
#     week: NFLWeek
#     venue: NFLVenue
#     home: NFLTeam
#     away: NFLTeam
    
@dataclass
class NFLGame:
    id: Key[str]
    status: str
    coverage: str
    game_type: str
    conference_game: bool
    scheduled: datetime
    entry_mode: str
    wx_temp: int
    wx_humidity: int
    wx_wind_speed: int
    wx_wind_direction: str
    wx_condition: str
    weather: str
    quarter: int
    clock: str
    sr_id: str

## ------------------DRIVE CONTEXT------------------##
@dataclass 
class NFLPeriod:
    id: Key[str]
    sequence: Key[int]
    number: int

## ------------------EVENT PAYLOAD (PLAYS)------------------##

@dataclass
class NFLDrive:
    id: Key[str]
    sequence: Key[int]
    team_sequence: Key[int]
    start_reason: str
    end_reason: str
    play_count: int
    duration: str
    start_clock: str
    end_clock: str
    first_downs: int
    gain: int
    first_drive_yardline: Optional[int]
    last_drive_yardline: Optional[int]
    farthest_drive_yardline: Optional[int]
    penalty_yards: int
    net_yards: int
    pat_points_attempted: int
    

## ------------------PLAY LOCATION & POSSESSION------------------##
@dataclass
class NFLPlayLocation:
    yardline: int
    name: Optional[str]
    market: Optional[str]
    alias: Optional[str]
    id: Key[str]
    sr_id: Key[str]
    
@dataclass
class NFLEventSituation:
    clock: Key[str]
    down: int
    yfd: int
    possession: NFLTeam
    location: NFLPlayLocation
    
## ------------------PLAYERS ------------------##
@dataclass
class NFLPlayer:
    name: str
    id: Key[str]
    jersey: str
    position: str
    role: Optional[str]
    sr_id: str

    
## ------------------ONE GLOBAL STATISTIC TYPE------------------##
@moose_data_model
@dataclass
class NFLStatistic:
    stat_type: Key[str]
    category: Optional[str]
    team: NFLTeam
    player: NFLPlayer
    
    # Generic fields
    attempt: Optional[int]
    yards: Optional[int]
    nullified: Optional[bool]
    firstdown: Optional[int]
    touchdown: Optional[int]
    safety: Optional[int]
    
    # Specific fields (all optional)
    block: Optional[int]
    complete: Optional[int]
    ast_sack: Optional[int]
    ast_tackle: Optional[int]
    ast_tlost: Optional[int]
    batted_pass: Optional[int]
    blitz: Optional[int]
    def_comp: Optional[int] ## docs say string but might be an int
    def_target: Optional[int]
    forced_fumble: Optional[int]
    hurry: Optional[int]
    interception: Optional[int]
    int_touchdown: Optional[int]
    int_yards: Optional[int]
    knockdown: Optional[int]
    missed_tackle: Optional[int]
    pass_defended: Optional[int]
    primary: Optional[int]
    qb_hit: Optional[int]
    sack: Optional[int]
    sack_yards: Optional[int]
    tlost: Optional[int]
    tlost_yards: Optional[int]
    tackle: Optional[int]
    down: Optional[int]
    ##first_down: Optional[FirstDown]
    aborted: Optional[int]
    blocked: Optional[int]
    made: Optional[int]
    missed: Optional[int]
    returned: Optional[int]
    att_yards: Optional[int]
    forced: Optional[int]
    fumble: Optional[int]
    lost: Optional[int]
    opp_rec: Optional[int]
    opp_rec_td: Optional[int]
    opp_rec_yards: Optional[int]
    out_of_bounds: Optional[int]
    own_rec: Optional[int]
    own_rec_td: Optional[int]
    own_rec_yards: Optional[int]
    play_category: Optional[str]
    endzone: Optional[int]
    inside_20: Optional[int]
    net_yards: Optional[int]
    onside_attempt: Optional[int]
    onside_success: Optional[int]
    squib_kick: Optional[int]
    touchback: Optional[int]
    goaltogo: Optional[int]
    incompletion_type: Optional[str]
    on_target_throw: Optional[int]
    pocket_time: Optional[float]
    penalty: Optional[int]
    downed: Optional[int]
    faircatch: Optional[int]
    hang_time: Optional[float]
    broken_tackles: Optional[int]
    catchable: Optional[int]
    dropped: Optional[int]
    reception: Optional[int]
    targets: Optional[int]
    yards_after_catch: Optional[int]
    yards_after_contact: Optional[int]
    lateral: Optional[int]
    play_type: Optional[str]
    kneel_down: Optional[int]
    scramble: Optional[int]
    
# ------------------PLAY DETAILS ------------------##

@dataclass 
class NFLPlayDetails:
    category: Key[str]
    description: Optional[str]
    yards: Optional[int]
    result: Optional[str]
    alt_description: Optional[str]
    start_location: NFLPlayLocation
    end_location: NFLPlayLocation
    sequence: Key[int]
    team: NFLTeam
    players: list[NFLPlayer]
    direction: Optional[str]
    sack_split: Optional[str]
    reason_missed: Optional[str]
    onside: Optional[str]
    no_attempt: Optional[str]
    
    
# # ------------------EVENT PAYLOAD (PLAYS)------------------##
@moose_data_model
@dataclass
class NFLPlay:
    game_id: Key[str]
    id: Key[str]
    type: str
    event_type: str
    home_team: NFLTeam
    away_team: NFLTeam
    sequence: Key[int]
    clock: str
    created_at: datetime
    updated_at: datetime
    home_points: Optional[int]
    away_points: Optional[int]
    wall_clock: Optional[datetime]
    description: str
    period: NFLPeriod
    drive: NFLDrive
    start_situation: NFLEventSituation
    end_situation: NFLEventSituation
    statistics: list[NFLStatistic]
    details: list[NFLPlayDetails]
    

    