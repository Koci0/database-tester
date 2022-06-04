create table drivers
(
    "driverId"  int primary key,
    code        text,
    dob         text,
    "driverRef" text,
    forename    text,
    nationality text,
    number      int,
    surname     text,
    url         text
);

INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (849, 'LAT', '1995-06-29', 'latifi', 'Nicholas', 'Canadian', 6, 'Latifi', 'http://en.wikipedia.org/wiki/Nicholas_Latifi');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (836, 'WEH', '1994-10-18', 'wehrlein', 'Pascal', 'German', 94, 'Wehrlein', 'http://en.wikipedia.org/wiki/Pascal_Wehrlein');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (844, 'LEC', '1997-10-16', 'leclerc', 'Charles', 'Monegasque', 16, 'Leclerc', 'http://en.wikipedia.org/wiki/Charles_Leclerc');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (838, 'VAN', '1992-03-26', 'vandoorne', 'Stoffel', 'Belgian', 2, 'Vandoorne', 'http://en.wikipedia.org/wiki/Stoffel_Vandoorne');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (818, 'VER', '1990-04-25', 'vergne', 'Jean-Éric', 'French', 25, 'Vergne', 'http://en.wikipedia.org/wiki/Jean-%C3%89ric_Vergne');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (831, 'NAS', '1992-08-21', 'nasr', 'Felipe', 'Brazilian', 12, 'Nasr', 'http://en.wikipedia.org/wiki/Felipe_Nasr');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (843, 'HAR', '1989-11-10', 'brendon_hartley', 'Brendon', 'New Zealander', 28, 'Hartley', 'http://en.wikipedia.org/wiki/Brendon_Hartley');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (822, 'BOT', '1989-08-28', 'bottas', 'Valtteri', 'Finnish', 77, 'Bottas', 'http://en.wikipedia.org/wiki/Valtteri_Bottas');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (824, 'BIA', '1989-08-03', 'jules_bianchi', 'Jules', 'French', 17, 'Bianchi', 'http://en.wikipedia.org/wiki/Jules_Bianchi');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (820, 'CHI', '1991-04-21', 'chilton', 'Max', 'British', 4, 'Chilton', 'http://en.wikipedia.org/wiki/Max_Chilton');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (828, 'ERI', '1990-09-02', 'ericsson', 'Marcus', 'Swedish', 9, 'Ericsson', 'http://en.wikipedia.org/wiki/Marcus_Ericsson');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (837, 'HAR', '1993-01-22', 'haryanto', 'Rio', 'Indonesian', 88, 'Haryanto', 'http://en.wikipedia.org/wiki/Rio_Haryanto');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (16, 'SUT', '1983-01-11', 'sutil', 'Adrian', 'German', 99, 'Sutil', 'http://en.wikipedia.org/wiki/Adrian_Sutil');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (835, 'PAL', '1991-01-20', 'jolyon_palmer', 'Jolyon', 'British', 30, 'Palmer', 'http://en.wikipedia.org/wiki/Jolyon_Palmer');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (852, 'TSU', '2000-05-11', 'tsunoda', 'Yuki', 'Japanese', 22, 'Tsunoda', 'http://en.wikipedia.org/wiki/Yuki_Tsunoda');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (840, 'STR', '1998-10-29', 'stroll', 'Lance', 'Canadian', 18, 'Stroll', 'http://en.wikipedia.org/wiki/Lance_Stroll');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (13, 'MAS', '1981-04-25', 'massa', 'Felipe', 'Brazilian', 19, 'Massa', 'http://en.wikipedia.org/wiki/Felipe_Massa');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (848, 'ALB', '1996-03-23', 'albon', 'Alexander', 'Thai', 23, 'Albon', 'http://en.wikipedia.org/wiki/Alexander_Albon');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (851, 'AIT', '1995-09-23', 'aitken', 'Jack', 'British', 89, 'Aitken', 'http://en.wikipedia.org/wiki/Jack_Aitken');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (854, 'MSC', '1999-03-22', 'mick_schumacher', 'Mick', 'German', 47, 'Schumacher', 'http://en.wikipedia.org/wiki/Mick_Schumacher');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (1, 'HAM', '1985-01-07', 'hamilton', 'Lewis', 'British', 44, 'Hamilton', 'http://en.wikipedia.org/wiki/Lewis_Hamilton');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (813, 'MAL', '1985-03-09', 'maldonado', 'Pastor', 'Venezuelan', 13, 'Maldonado', 'http://en.wikipedia.org/wiki/Pastor_Maldonado');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (8, 'RAI', '1979-10-17', 'raikkonen', 'Kimi', 'Finnish', 7, 'Räikkönen', 'http://en.wikipedia.org/wiki/Kimi_R%C3%A4ikk%C3%B6nen');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (855, 'ZHO', '1999-05-30', 'zhou', 'Guanyu', 'Chinese', 24, 'Zhou', 'http://en.wikipedia.org/wiki/Guanyu_Zhou');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (841, 'GIO', '1993-12-14', 'giovinazzi', 'Antonio', 'Italian', 99, 'Giovinazzi', 'http://en.wikipedia.org/wiki/Antonio_Giovinazzi');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (4, 'ALO', '1981-07-29', 'alonso', 'Fernando', 'Spanish', 14, 'Alonso', 'http://en.wikipedia.org/wiki/Fernando_Alonso');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (18, 'BUT', '1980-01-19', 'button', 'Jenson', 'British', 22, 'Button', 'http://en.wikipedia.org/wiki/Jenson_Button');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (845, 'SIR', '1995-08-27', 'sirotkin', 'Sergey', 'Russian', 35, 'Sirotkin', 'http://en.wikipedia.org/wiki/Sergey_Sirotkin_(racing_driver)');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (834, 'RSS', '1991-09-25', 'rossi', 'Alexander', 'American', 53, 'Rossi', 'http://en.wikipedia.org/wiki/Alexander_Rossi_%28racing_driver%29');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (155, 'KOB', '1986-09-13', 'kobayashi', 'Kamui', 'Japanese', 10, 'Kobayashi', 'http://en.wikipedia.org/wiki/Kamui_Kobayashi');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (833, 'MER', '1991-03-22', 'merhi', 'Roberto', 'Spanish', 98, 'Merhi', 'http://en.wikipedia.org/wiki/Roberto_Merhi');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (847, 'RUS', '1998-02-15', 'russell', 'George', 'British', 63, 'Russell', 'http://en.wikipedia.org/wiki/George_Russell_%28racing_driver%29');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (825, 'MAG', '1992-10-05', 'kevin_magnussen', 'Kevin', 'Danish', 20, 'Magnussen', 'http://en.wikipedia.org/wiki/Kevin_Magnussen');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (827, 'LOT', '1981-11-19', 'lotterer', 'André', 'German', 45, 'Lotterer', 'http://en.wikipedia.org/wiki/Andr%C3%A9_Lotterer');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (815, 'PER', '1990-01-26', 'perez', 'Sergio', 'Mexican', 11, 'Pérez', 'http://en.wikipedia.org/wiki/Sergio_P%C3%A9rez');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (853, 'MAZ', '1999-03-02', 'mazepin', 'Nikita', 'Russian', 9, 'Mazepin', 'http://en.wikipedia.org/wiki/Nikita_Mazepin');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (20, 'VET', '1987-07-03', 'vettel', 'Sebastian', 'German', 5, 'Vettel', 'http://en.wikipedia.org/wiki/Sebastian_Vettel');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (846, 'NOR', '1999-11-13', 'norris', 'Lando', 'British', 4, 'Norris', 'http://en.wikipedia.org/wiki/Lando_Norris');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (826, 'KVY', '1994-04-26', 'kvyat', 'Daniil', 'Russian', 26, 'Kvyat', 'http://en.wikipedia.org/wiki/Daniil_Kvyat');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (830, 'VER', '1997-09-30', 'max_verstappen', 'Max', 'Dutch', 33, 'Verstappen', 'http://en.wikipedia.org/wiki/Max_Verstappen');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (842, 'GAS', '1996-02-07', 'gasly', 'Pierre', 'French', 10, 'Gasly', 'http://en.wikipedia.org/wiki/Pierre_Gasly');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (9, 'KUB', '1984-12-07', 'kubica', 'Robert', 'Polish', 88, 'Kubica', 'http://en.wikipedia.org/wiki/Robert_Kubica');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (839, 'OCO', '1996-09-17', 'ocon', 'Esteban', 'French', 31, 'Ocon', 'http://en.wikipedia.org/wiki/Esteban_Ocon');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (850, 'FIT', '1996-06-25', 'pietro_fittipaldi', 'Pietro', 'Brazilian', 51, 'Fittipaldi', 'http://en.wikipedia.org/wiki/Pietro_Fittipaldi');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (821, 'GUT', '1991-08-05', 'gutierrez', 'Esteban', 'Mexican', 21, 'Gutiérrez', 'http://en.wikipedia.org/wiki/Esteban_Guti%C3%A9rrez');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (817, 'RIC', '1989-07-01', 'ricciardo', 'Daniel', 'Australian', 3, 'Ricciardo', 'http://en.wikipedia.org/wiki/Daniel_Ricciardo');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (154, 'GRO', '1986-04-17', 'grosjean', 'Romain', 'French', 8, 'Grosjean', 'http://en.wikipedia.org/wiki/Romain_Grosjean');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (807, 'HUL', '1987-08-19', 'hulkenberg', 'Nico', 'German', 27, 'Hülkenberg', 'http://en.wikipedia.org/wiki/Nico_H%C3%BClkenberg');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (832, 'SAI', '1994-09-01', 'sainz', 'Carlos', 'Spanish', 55, 'Sainz', 'http://en.wikipedia.org/wiki/Carlos_Sainz_Jr.');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (829, 'STE', '1991-06-28', 'stevens', 'Will', 'British', 28, 'Stevens', 'http://en.wikipedia.org/wiki/Will_Stevens');
INSERT INTO f1_data.drivers ("driverId", code, dob, "driverRef", forename, nationality, number, surname, url) VALUES (3, 'ROS', '1985-06-27', 'rosberg', 'Nico', 'German', 6, 'Rosberg', 'http://en.wikipedia.org/wiki/Nico_Rosberg');
