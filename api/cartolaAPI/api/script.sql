CREATE TABLE IF NOT EXISTS `mydb`.`TB_UCLUB` (
  `id_uclub` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NOT NULL,
  `color1` VARCHAR(7) NULL DEFAULT '#FF0000',
  `color2` VARCHAR(7) NULL DEFAULT '#FFFFFF',
  `color3` VARCHAR(7) NULL DEFAULT '#000000',
  `crest` INT NULL DEFAULT 0,
  `networth` INT NOT NULL DEFAULT 100,
  `id_owner` INT NOT NULL,
  PRIMARY KEY (`id_uclub`),
  INDEX `fk_TB_UCLUB_TB_USER_idx` (`id_owner` ASC),
  CONSTRAINT `fk_TB_UCLUB_TB_USER`
    FOREIGN KEY (`id_owner`)
    REFERENCES `mydb`.`TB_USER` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_R_CLUB`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_R_CLUB` (
  `id_rclub` INT NOT NULL AUTO_INCREMENT,
  `crest` LONGBLOB NULL,
  `nome` VARCHAR(60) NULL,
  `short_name` VARCHAR(3) NULL,
  PRIMARY KEY (`id_rclub`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_POSITION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_POSITION` (
  `cod_pos` VARCHAR(3) NOT NULL,
  `nome` VARCHAR(45) NULL,
  PRIMARY KEY (`cod_pos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_PLAYER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_PLAYER` (
  `id_player` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(60) NULL,
  `id_club` INT NOT NULL,
  `cod_pos` VARCHAR(3) NOT NULL,
  PRIMARY KEY (`id_player`, `cod_pos`),
  INDEX `fk_TB_PLAYER_TB_R_CLUB1_idx` (`id_club` ASC),
  INDEX `fk_TB_PLAYER_TB_POSITION1_idx` (`cod_pos` ASC),
  CONSTRAINT `fk_TB_PLAYER_TB_R_CLUB1`
    FOREIGN KEY (`id_club`)
    REFERENCES `mydb`.`TB_R_CLUB` (`id_rclub`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_PLAYER_TB_POSITION1`
    FOREIGN KEY (`cod_pos`)
    REFERENCES `mydb`.`TB_POSITION` (`cod_pos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_ROUND`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_ROUND` (
  `round_number` INT NOT NULL,
  `season` INT NOT NULL,
  `id_round` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_round`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_MATCH`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_MATCH` (
  `id_match` INT NOT NULL AUTO_INCREMENT,
  `datetime` DATETIME NULL,
  `home_score` INT NULL,
  `away_score` INT NULL,
  `home_club` INT NOT NULL,
  `away_club` INT NOT NULL,
  `id_round` INT NOT NULL,
  PRIMARY KEY (`id_match`, `id_round`),
  INDEX `fk_TB_MATCH_TB_R_CLUB1_idx` (`home_club` ASC),
  INDEX `fk_TB_MATCH_TB_R_CLUB2_idx` (`away_club` ASC),
  INDEX `fk_TB_MATCH_TB_ROUND1_idx` (`id_round` ASC),
  CONSTRAINT `fk_TB_MATCH_TB_R_CLUB1`
    FOREIGN KEY (`home_club`)
    REFERENCES `mydb`.`TB_R_CLUB` (`id_rclub`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_MATCH_TB_R_CLUB2`
    FOREIGN KEY (`away_club`)
    REFERENCES `mydb`.`TB_R_CLUB` (`id_rclub`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_MATCH_TB_ROUND1`
    FOREIGN KEY (`id_round`)
    REFERENCES `mydb`.`TB_ROUND` (`id_round`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_FORMATION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_FORMATION` (
  `id_fmt` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(5) NULL,
  PRIMARY KEY (`id_fmt`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_STAT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_STAT` (
  `id_stat` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NULL,
  `desc` VARCHAR(300) NULL,
  `points` DECIMAL ZEROFILL NULL,
  PRIMARY KEY (`id_stat`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_LEAGUE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_LEAGUE` (
  `id_league` INT NOT NULL AUTO_INCREMENT,
  `color1` VARCHAR(7) NULL DEFAULT '#FF0000',
  `color2` VARCHAR(7) NULL DEFAULT '#FFFFFF',
  `color3` VARCHAR(7) NULL DEFAULT '#000000',
  `crest` INT ZEROFILL NULL,
  `id_creator` INT NOT NULL,
  PRIMARY KEY (`id_league`),
  INDEX `fk_TB_LEAGUE_TB_USER1_idx` (`id_creator` ASC),
  CONSTRAINT `fk_TB_LEAGUE_TB_USER1`
    FOREIGN KEY (`id_creator`)
    REFERENCES `mydb`.`TB_USER` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_FMT_POS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_FMT_POS` (
  `id_fmt` INT NOT NULL,
  `cod_pos` VARCHAR(3) NOT NULL,
  `amount` INT ZEROFILL NULL,
  PRIMARY KEY (`id_fmt`, `cod_pos`),
  INDEX `fk_TB_FORMATION_has_TB_POSITION_TB_POSITION1_idx` (`cod_pos` ASC),
  INDEX `fk_TB_FORMATION_has_TB_POSITION_TB_FORMATION1_idx` (`id_fmt` ASC),
  CONSTRAINT `fk_TB_FORMATION_has_TB_POSITION_TB_FORMATION1`
    FOREIGN KEY (`id_fmt`)
    REFERENCES `mydb`.`TB_FORMATION` (`id_fmt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_FORMATION_has_TB_POSITION_TB_POSITION1`
    FOREIGN KEY (`cod_pos`)
    REFERENCES `mydb`.`TB_POSITION` (`cod_pos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_PLAYER_STAT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_PLAYER_STAT` (
  `id_player` INT NOT NULL,
  `id_stat` INT NOT NULL,
  `id_round` INT NOT NULL,
  PRIMARY KEY (`id_player`, `id_stat`, `id_round`),
  INDEX `fk_TB_PLAYER_has_TB_STAT_TB_STAT1_idx` (`id_stat` ASC),
  INDEX `fk_TB_PLAYER_has_TB_STAT_TB_PLAYER1_idx` (`id_player` ASC),
  INDEX `fk_TB_PLAYER_STAT_TB_ROUND1_idx` (`id_round` ASC),
  CONSTRAINT `fk_TB_PLAYER_has_TB_STAT_TB_PLAYER1`
    FOREIGN KEY (`id_player`)
    REFERENCES `mydb`.`TB_PLAYER` (`id_player`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_PLAYER_has_TB_STAT_TB_STAT1`
    FOREIGN KEY (`id_stat`)
    REFERENCES `mydb`.`TB_STAT` (`id_stat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_PLAYER_STAT_TB_ROUND1`
    FOREIGN KEY (`id_round`)
    REFERENCES `mydb`.`TB_ROUND` (`id_round`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_SQUAD`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_SQUAD` (
  `id_club` INT NOT NULL,
  `id_fmt` INT NOT NULL,
  `id_round` INT NOT NULL,
  PRIMARY KEY (`id_club`, `id_round`),
  INDEX `fk_TB_UCLUB_has_TB_FORMATION_TB_FORMATION1_idx` (`id_fmt` ASC),
  INDEX `fk_TB_UCLUB_has_TB_FORMATION_TB_UCLUB1_idx` (`id_club` ASC),
  INDEX `fk_TB_UCLUB_has_TB_FORMATION_TB_ROUND1_idx` (`id_round` ASC),
  CONSTRAINT `fk_TB_UCLUB_has_TB_FORMATION_TB_UCLUB1`
    FOREIGN KEY (`id_club`)
    REFERENCES `mydb`.`TB_UCLUB` (`id_uclub`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_UCLUB_has_TB_FORMATION_TB_FORMATION1`
    FOREIGN KEY (`id_fmt`)
    REFERENCES `mydb`.`TB_FORMATION` (`id_fmt`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_UCLUB_has_TB_FORMATION_TB_ROUND1`
    FOREIGN KEY (`id_round`)
    REFERENCES `mydb`.`TB_ROUND` (`id_round`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_SELECTED`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_SELECTED` (
  `id_club` INT NOT NULL,
  `id_round` INT NOT NULL,
  `id_player` INT NOT NULL,
  PRIMARY KEY (`id_club`, `id_round`, `id_player`),
  INDEX `fk_TB_SQUAD_has_TB_PLAYER_TB_PLAYER1_idx` (`id_player` ASC),
  INDEX `fk_TB_SQUAD_has_TB_PLAYER_TB_SQUAD1_idx` (`id_club` ASC, `id_round` ASC),
  CONSTRAINT `fk_TB_SQUAD_has_TB_PLAYER_TB_SQUAD1`
    FOREIGN KEY (`id_club` , `id_round`)
    REFERENCES `mydb`.`TB_SQUAD` (`id_club` , `id_round`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_SQUAD_has_TB_PLAYER_TB_PLAYER1`
    FOREIGN KEY (`id_player`)
    REFERENCES `mydb`.`TB_PLAYER` (`id_player`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_CLUB_LEAGUE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_CLUB_LEAGUE` (
  `id_club` INT NOT NULL,
  `id_league` INT NOT NULL,
  PRIMARY KEY (`id_club`, `id_league`),
  INDEX `fk_TB_UCLUB_has_TB_LEAGUE_TB_LEAGUE1_idx` (`id_league` ASC),
  INDEX `fk_TB_UCLUB_has_TB_LEAGUE_TB_UCLUB1_idx` (`id_club` ASC),
  CONSTRAINT `fk_TB_UCLUB_has_TB_LEAGUE_TB_UCLUB1`
    FOREIGN KEY (`id_club`)
    REFERENCES `mydb`.`TB_UCLUB` (`id_uclub`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_UCLUB_has_TB_LEAGUE_TB_LEAGUE1`
    FOREIGN KEY (`id_league`)
    REFERENCES `mydb`.`TB_LEAGUE` (`id_league`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TB_PLAYER_PRICE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`TB_PLAYER_PRICE` (
  `id_player` INT NOT NULL,
  `id_round` INT NOT NULL,
  `price` INT ZEROFILL NULL,
  `captain` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id_player`, `id_round`),
  INDEX `fk_TB_PLAYER_has_TB_ROUND_TB_ROUND1_idx` (`id_round` ASC),
  INDEX `fk_TB_PLAYER_has_TB_ROUND_TB_PLAYER1_idx` (`id_player` ASC),
  CONSTRAINT `fk_TB_PLAYER_has_TB_ROUND_TB_PLAYER1`
    FOREIGN KEY (`id_player`)
    REFERENCES `mydb`.`TB_PLAYER` (`id_player`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TB_PLAYER_has_TB_ROUND_TB_ROUND1`
    FOREIGN KEY (`id_round`)
    REFERENCES `mydb`.`TB_ROUND` (`id_round`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

