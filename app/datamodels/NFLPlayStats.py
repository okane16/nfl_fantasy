# from moose_lib import moose_data_model, Key
# from typing import Optional
# from dataclasses import dataclass

# ## ------------------STATISTICS BY PLAY TYPE------------------##
# @dataclass
# class Block:
#     stat_type: Key[str]
#     block: int
#     category: str
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class Conversion:
#     stat_type: Key[str]
#     attempt: int
#     category: str
#     complete: int
#     safety: int
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class Defense:
#     stat_type: Key[str]
#     ast_sack: Optional[int]
#     ast_tackle: Optional[int]
#     ast_tlost: Optional[int]
#     batted_pass: Optional[int]
#     blitz: Optional[int]
#     block: Optional[int]
#     category: str
#     def_comp: Optional[str]
#     def_target: Optional[int]
#     forced_fumble: Optional[int]
#     hurry: Optional[int]
#     interception: Optional[int]
#     int_touchdown: Optional[int]
#     int_yards: Optional[int]
#     knockdown: Optional[int]
#     missed_tackle: Optional[int]
#     nullified: Optional[bool]
#     pass_defended: Optional[int]
#     primary: Optional[int]
#     qb_hit: Optional[int]
#     sack: Optional[int]
#     sack_yards: Optional[int]
#     safety: Optional[int]
#     tlost: Optional[int]
#     tlost_yards: Optional[int]
#     tackle: Optional[int]
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class DefenseConversion:
#     stat_type: Key[str]
#     attempt: int
#     category: str
#     complete: int
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class FirstDown:
#     stat_type: Key[str]
#     category: str
#     team: NFLTeam
#     player: NFLPlayer
    
# @dataclass
# class DownConversion:
#     stat_type: Key[str]
#     attempt: int
#     complete: str
#     down: int
#     first_down: FirstDown
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class ExtraPoint:
#     stat_type: Key[str]
#     aborted: int
#     attempt: int
#     blocked: int
#     made: int
#     missed: int
#     returned: int
#     safety: int
#     team: NFLTeam
#     player: NFLPlayer
    
# @dataclass
# class FieldGoal:
#     stat_type: Key[str]
#     attempt: int
#     att_yards: int
#     blocked: int
#     made: int
#     missed: int
#     nullified: bool
#     returned: int
#     yards: int
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass 
# class Fumble:
#     stat_type: Key[str]
#     forced: int
#     fumble: int
#     lost: int
#     nullified: bool
#     opp_rec: int
#     opp_rec_td: int
#     opp_rec_yards: int
#     out_of_bounds: int
#     own_rec: int
#     own_rec_td: int
#     own_rec_yards: int
#     play_category: str
#     team: NFLTeam
#     player: NFLPlayer
    
# @dataclass
# class Kickoff:
#     stat_type: Key[str]
#     attempt: int
#     endzone: int
#     inside_20: int
#     net_yards: int
#     nullified: bool
#     onside_attempt: int
#     onside_success: int
#     own_rec: int
#     own_rec_td: int
#     squib_kick: int
#     touchback: int
#     yards: int
#     team: NFLTeam
#     player: NFLPlayer 
       
# @dataclass
# class Pass:
#     stat_type: Key[str]
#     attempt: int
#     att_yards: int
#     batted_pass: int
#     blitz: int
#     complete: int
#     firstdown: int
#     goaltogo: int
#     hurry: int
#     incompletion_type: str
#     inside_20: int
#     interception: int
#     int_touchdown: int
#     knockdown: int
#     nullified: bool
#     on_target_throw: int
#     pocket_time: float
#     sack: int
#     sack_yards: int
#     safety: int
#     touchdown: int
#     yards: int
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class Penalty:
#     stat_type: Key[str]
#     category: Optional[str]
#     penalty: int
#     yards: int
#     team: NFLTeam
#     player: NFLPlayer

# @dataclass
# class Punt:
#     stat_type: Key[str]
#     attempt: int
#     blocked: int
#     downed: int
#     endzone: int
#     faircatch: int
#     hang_time: float
#     inside_20: int
#     net_yards: int
#     nullified: bool
#     out_of_bounds: int
#     touchback: int
#     yards: int
#     team: NFLTeam
#     player: NFLPlayer
    
# @dataclass
# class Receive:
#     stat_type: Key[str]
#     broken_tackles: int
#     catchable: int
#     dropped: int
#     firstdown: int
#     goaltogo: int
#     inside_20: int
#     nullified: bool
#     reception: int
#     safety: int
#     targets: int
#     touchdown: int
#     yards: int
#     yards_after_catch: int
#     yards_after_contact: int
#     team: NFLTeam
#     player: NFLPlayer
    
# @dataclass
# class Return:
#     stat_type: Key[str]
#     category: str
#     downed: int
#     faircatch: int
#     firstdown: int
#     lateral: int
#     nullified: bool
#     out_of_bounds: int
#     play_type: str
#     touchback: int
#     touchdown: int
#     yards: int
#     team: NFLTeam
#     player: NFLPlayer
    
# @dataclass
# class Rush:
#     stat_type: Key[str]
#     attempt: int
#     broken_tackles: int
#     firstdown: int
#     goaltogo: int
#     inside_20: int
#     kneel_down: int
#     lateral: int
#     nullified: bool
#     safety: int
#     scramble: int
#     tlost: int
#     tlost_yards: int
#     touchdown: int
#     yards: int
#     yards_after_contact: int  
#     team: NFLTeam
#     player: NFLPlayer