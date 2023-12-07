const URLSTAT_LIST = [
  "keepers",
  "shooting",
  "keepersadv",
  "passing",
  "gca",
  "defense",
  "possession",
  "playingtime",
  "misc",
];
const URLSTAT_TO_TABLEID_MAP_PLAYERS = {
  keepers: "stats_keeper",
  shooting: "stats_shooting",
  keepersadv: "stats_keeper_adv",
  passing: "stats_passing",
  gca: "stats_gca",
  defense: "stats_defense",
  possession: "stats_possession",
  playingtime: "stats_playing_time",
  misc: "stats_misc",
};
const URLSTAT_TO_TABLEID_MAP_SQUAD = {
  keepers: "stats_squads_keeper_for",
  shooting: "stats_squads_shooting_for",
  keepersadv: "stats_squads_keeper_adv_for",
  passing: "stats_squads_passing_for",
  gca: "stats_squads_gca_for",
  defense: "stats_squads_defense_for",
  possession: "stats_squads_possession_for",
  playingtime: "stats_squads_playing_time_for",
  misc: "stats_squads_misc_for",
};

const LEAGUE_LIST = [
  "Premier-League-Stats",
  "La-Liga-Stats",
  "Bundesliga-Stats",
  "Serie-A-Stats",
  "Ligue-1-Stats",
];

const LEAGUE_TO_ID = {
  "Premier-League-Stats": 9,
  "La-Liga-Stats": 12,
  "Bundesliga-Stats": 20,
  "Serie-A-Stats": 11,
  "Ligue-1-Stats": 13,
};

const SEASON_LIST = [
  "2018-2019",
  "2019-2020",
  "2020-2021",
  "2021-2022",
  "2022-2023",
];

module.exports = {
  URLSTAT_LIST,
  LEAGUE_LIST,
  LEAGUE_TO_ID,
  SEASON_LIST,
  URLSTAT_TO_TABLEID_MAP_PLAYERS,
  URLSTAT_TO_TABLEID_MAP_SQUAD,
};
