BEGIN TRANSACTION;
DROP TABLE IF EXISTS "api_clubleague";
CREATE TABLE IF NOT EXISTS "api_clubleague" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"club_id"	integer,
	"league_id"	integer,
	FOREIGN KEY("league_id") REFERENCES "api_league"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("club_id") REFERENCES "api_userclub"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_fmtpos";
CREATE TABLE IF NOT EXISTS "api_fmtpos" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"amount"	integer,
	"formation_id"	integer,
	"position_id"	integer,
	FOREIGN KEY("position_id") REFERENCES "api_position"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("formation_id") REFERENCES "api_formation"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_league";
CREATE TABLE IF NOT EXISTS "api_league" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"color1"	varchar(7),
	"color2"	varchar(7),
	"color3"	varchar(7),
	"crest"	varchar(100),
	"creator_id"	integer,
	FOREIGN KEY("creator_id") REFERENCES "api_usuario"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_match";
CREATE TABLE IF NOT EXISTS "api_match" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"datetime"	datetime,
	"home_score"	integer,
	"away_score"	integer,
	"_round_id"	integer,
	"away_club_id"	integer,
	"home_club_id"	integer,
	FOREIGN KEY("home_club_id") REFERENCES "api_realclub"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("_round_id") REFERENCES "api_round"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("away_club_id") REFERENCES "api_realclub"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_player";
CREATE TABLE IF NOT EXISTS "api_player" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	varchar(60),
	"club_id"	integer,
	"position_id"	integer,
	FOREIGN KEY("position_id") REFERENCES "api_position"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("club_id") REFERENCES "api_realclub"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_playerprice";
CREATE TABLE IF NOT EXISTS "api_playerprice" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"price"	integer,
	"captain"	smallint,
	"_round_id"	integer,
	"player_id"	integer,
	FOREIGN KEY("player_id") REFERENCES "api_player"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("_round_id") REFERENCES "api_round"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_playerstats";
CREATE TABLE IF NOT EXISTS "api_playerstats" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"_round_id"	integer,
	"player_id"	integer,
	"stat_id"	integer,
	FOREIGN KEY("player_id") REFERENCES "api_player"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("stat_id") REFERENCES "api_stat"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("_round_id") REFERENCES "api_round"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_selected";
CREATE TABLE IF NOT EXISTS "api_selected" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"_round_id"	integer,
	"club_id"	integer,
	"player_id"	integer,
	FOREIGN KEY("player_id") REFERENCES "api_player"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("club_id") REFERENCES "api_userclub"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("_round_id") REFERENCES "api_round"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_squad";
CREATE TABLE IF NOT EXISTS "api_squad" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"_round_id"	integer,
	"club_id"	integer,
	"fmt_id"	integer,
	FOREIGN KEY("club_id") REFERENCES "api_userclub"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("fmt_id") REFERENCES "api_fmtpos"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("_round_id") REFERENCES "api_round"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_userclub";
CREATE TABLE IF NOT EXISTS "api_userclub" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	varchar(60),
	"color1"	varchar(7),
	"color2"	varchar(7),
	"color3"	varchar(7),
	"crest"	varchar(100),
	"owner_id"	integer,
	FOREIGN KEY("owner_id") REFERENCES "api_usuario"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "api_stat";
CREATE TABLE IF NOT EXISTS "api_stat" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	varchar(60),
	"desc"	varchar(300),
	"points"	decimal
);
DROP TABLE IF EXISTS "api_round";
CREATE TABLE IF NOT EXISTS "api_round" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"round_number"	integer,
	"season"	integer
);
DROP TABLE IF EXISTS "api_realclub";
CREATE TABLE IF NOT EXISTS "api_realclub" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	varchar(60),
	"crest"	varchar(100),
	"short_name"	varchar(3)
);
DROP TABLE IF EXISTS "api_position";
CREATE TABLE IF NOT EXISTS "api_position" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	varchar(60),
	"cod_pos"	varchar(3)
);
DROP TABLE IF EXISTS "api_formation";
CREATE TABLE IF NOT EXISTS "api_formation" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	varchar(5)
);
DROP TABLE IF EXISTS "api_usuario";
CREATE TABLE IF NOT EXISTS "api_usuario" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"email"	varchar(255) NOT NULL UNIQUE,
	"name"	varchar(255) NOT NULL,
	"foto"	varchar(100),
	"is_active"	bool NOT NULL,
	"first_access"	bool NOT NULL,
	"is_admin"	bool NOT NULL,
	"birthdate"	date
);
DROP INDEX IF EXISTS "api_clubleague_league_id_0d895277";
CREATE INDEX IF NOT EXISTS "api_clubleague_league_id_0d895277" ON "api_clubleague" (
	"league_id"
);
DROP INDEX IF EXISTS "api_clubleague_club_id_9edc33f2";
CREATE INDEX IF NOT EXISTS "api_clubleague_club_id_9edc33f2" ON "api_clubleague" (
	"club_id"
);
DROP INDEX IF EXISTS "api_fmtpos_position_id_c7a40f31";
CREATE INDEX IF NOT EXISTS "api_fmtpos_position_id_c7a40f31" ON "api_fmtpos" (
	"position_id"
);
DROP INDEX IF EXISTS "api_fmtpos_formation_id_1f63e671";
CREATE INDEX IF NOT EXISTS "api_fmtpos_formation_id_1f63e671" ON "api_fmtpos" (
	"formation_id"
);
DROP INDEX IF EXISTS "api_league_creator_id_3ed8b020";
CREATE INDEX IF NOT EXISTS "api_league_creator_id_3ed8b020" ON "api_league" (
	"creator_id"
);
DROP INDEX IF EXISTS "api_match_home_club_id_4a6e6a7d";
CREATE INDEX IF NOT EXISTS "api_match_home_club_id_4a6e6a7d" ON "api_match" (
	"home_club_id"
);
DROP INDEX IF EXISTS "api_match_away_club_id_c365fdcc";
CREATE INDEX IF NOT EXISTS "api_match_away_club_id_c365fdcc" ON "api_match" (
	"away_club_id"
);
DROP INDEX IF EXISTS "api_match__round_id_2f9bd887";
CREATE INDEX IF NOT EXISTS "api_match__round_id_2f9bd887" ON "api_match" (
	"_round_id"
);
DROP INDEX IF EXISTS "api_player_position_id_7cf6ee64";
CREATE INDEX IF NOT EXISTS "api_player_position_id_7cf6ee64" ON "api_player" (
	"position_id"
);
DROP INDEX IF EXISTS "api_player_club_id_a3e28cac";
CREATE INDEX IF NOT EXISTS "api_player_club_id_a3e28cac" ON "api_player" (
	"club_id"
);
DROP INDEX IF EXISTS "api_playerprice_player_id_436866d5";
CREATE INDEX IF NOT EXISTS "api_playerprice_player_id_436866d5" ON "api_playerprice" (
	"player_id"
);
DROP INDEX IF EXISTS "api_playerprice__round_id_316fb8af";
CREATE INDEX IF NOT EXISTS "api_playerprice__round_id_316fb8af" ON "api_playerprice" (
	"_round_id"
);
DROP INDEX IF EXISTS "api_playerstats_stat_id_fa4a2392";
CREATE INDEX IF NOT EXISTS "api_playerstats_stat_id_fa4a2392" ON "api_playerstats" (
	"stat_id"
);
DROP INDEX IF EXISTS "api_playerstats_player_id_a23d5698";
CREATE INDEX IF NOT EXISTS "api_playerstats_player_id_a23d5698" ON "api_playerstats" (
	"player_id"
);
DROP INDEX IF EXISTS "api_playerstats__round_id_5d80c05b";
CREATE INDEX IF NOT EXISTS "api_playerstats__round_id_5d80c05b" ON "api_playerstats" (
	"_round_id"
);
DROP INDEX IF EXISTS "api_selected_player_id_1cf34345";
CREATE INDEX IF NOT EXISTS "api_selected_player_id_1cf34345" ON "api_selected" (
	"player_id"
);
DROP INDEX IF EXISTS "api_selected_club_id_279cfda9";
CREATE INDEX IF NOT EXISTS "api_selected_club_id_279cfda9" ON "api_selected" (
	"club_id"
);
DROP INDEX IF EXISTS "api_selected__round_id_cb27e12b";
CREATE INDEX IF NOT EXISTS "api_selected__round_id_cb27e12b" ON "api_selected" (
	"_round_id"
);
DROP INDEX IF EXISTS "api_squad_fmt_id_6b2a3304";
CREATE INDEX IF NOT EXISTS "api_squad_fmt_id_6b2a3304" ON "api_squad" (
	"fmt_id"
);
DROP INDEX IF EXISTS "api_squad_club_id_2e387fe5";
CREATE INDEX IF NOT EXISTS "api_squad_club_id_2e387fe5" ON "api_squad" (
	"club_id"
);
DROP INDEX IF EXISTS "api_squad__round_id_04e2944d";
CREATE INDEX IF NOT EXISTS "api_squad__round_id_04e2944d" ON "api_squad" (
	"_round_id"
);
DROP INDEX IF EXISTS "api_userclub_owner_id_bfe4fed3";
CREATE INDEX IF NOT EXISTS "api_userclub_owner_id_bfe4fed3" ON "api_userclub" (
	"owner_id"
);
COMMIT;
