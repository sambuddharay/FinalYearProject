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
const URLSTAT_TO_TABLEID_MAP = {
  keepers: "stats_keeper",
  shooting: "stats_shooting",
  keepersadv: "stats_keeper_adv",
  passing: "stats_passing",
  passing_types: "stats_passing_types",
  gca: "stats_gca",
  defense: "stats_defense",
  possession: "stats_squads_possession_for",
  playingtime: "stats_playing_time",
  misc: "stats_misc",
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
  URLSTAT_TO_TABLEID_MAP,
};
