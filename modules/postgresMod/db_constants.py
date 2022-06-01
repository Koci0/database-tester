SEASONS_COLUMNS = {"YEAR": "year",
                   "URL": "url"}

STATUS_COLUMNS = {"STATUS_ID": "statusId",
                  "STATUS": "status"}

CIRCUITS_COLUMNS = {"CIRCUIT_ID": "circuitId",
                    "CIRCUIT_REF": "circuitRef",
                    "NAME": "name",
                    "LOCATION": "location",
                    "COUNTRY": "country",
                    "LAT": "lat",
                    "LNG": "lng",
                    "ALT": "alt",
                    "URL": "url"}

RACES_COLUMNS = {"RACE_ID": "raceId",
                 "YEAR": "year",
                 "ROUND": "round",
                 "CIRCUIT_ID": "circuitId",
                 "NAME": "name",
                 "DATE": "date",
                 "TIME": "time",
                 "URL": "url"}

PITSTOPS_COLUMNS = {"RACE_ID": "raceId",
                    "DRIVER_ID": "driverId",
                    "STOP": "stop",
                    "LAP": "lap",
                    "TIME": "time",
                    "DURATION": "duration",
                    "MILLISECONDS": "milliseconds"}

LAPTIMES_COLUMNS = {"RACE_ID": "raceId",
                    "DRIVER_ID": "driverId",
                    "LAP": "lap",
                    "POSITION": "position",
                    "TIME": "time",
                    "MILLISECONDS": "milliseconds"}

DRIVER_STANDINGS_COLUMNS = {"DRIVER_STANDINGS_ID": "driverStandingsId",
                            "RACE_ID": "raceId",
                            "DRIVER_ID": "driverId",
                            "POINTS": "points",
                            "POSITION": "position",
                            "POSITION_TEXT": "positionText",
                            "WINS": "wins"}

DRIVER_COLUMNS = {"DRIVER_ID": "driverId",
                  "DRIVER_REF": "driverRef",
                  "NUMBER": "number",
                  "CODE": "code",
                  "FORENAME": "forename",
                  "SURNAME": "surname",
                  "DOB": "dob",
                  "NATIONALITY": "nationality",
                  "URL": "url"}

QUALIFYING_COLUMNS = {"QUALIFY_ID": "qualifyId",
                      "RACE_ID": "raceId",
                      "DRIVER_ID": "driverId",
                      "CONSTRUCTOR_ID": "constructorId",
                      "NUMBER": "number",
                      "POSITION": "position",
                      "Q1": "q1",
                      "Q2": "q2",
                      "Q3": "q3"}

CONSTRUCTORS_COLUMNS = {"CONSTRUCTOR_ID": "constructorId",
                        "CONSTRUCTOR_REF": "constructorRef",
                        "NAME": "name",
                        "NATIONALITY": "nationality",
                        "URL": "url"}

CONSTRUCTOR_STANDINGS_COLUMNS = {"CONSTRUCTOR_STANDINGS_ID": "constructorStandingsId",
                                 "CONSTRUCTOR_ID": "constructorId",
                                 "RACE_ID": "raceId", "POINTS": "points",
                                 "POSITION": "position",
                                 "POSITION_TEXT": "positionText",
                                 "WINS": "wins"}

CONSTRUCTORS_RESULTS_COLUMNS = {"CONSTRUCTOR_RESULTS_ID": "constructorResultsId",
                                "RACE_ID": "raceId",
                                "CONSTRUCTOR_ID": "constructorId",
                                "POINTS": "points",
                                "STATUS": "status"}

RESULTS_COLUMNS = {"RESULT_ID": "resultId",
                   "RACE_ID": "raceId",
                   "CONSTRUCTOR_ID": "constructorId",
                   "DRIVER_ID": "driverId",
                   "NUMBER": "number",
                   "GRID": "grid",
                   "POSITION": "position",
                   "POSITION_TEXT": "positionText",
                   "POSITION_ORDER": "positionOrder",
                   "POINTS": "points",
                   "LAPS": "laps",
                   "TIME": "time",
                   "MILLISECONDS": "milliseconds",
                   "FASTEST_LAP": "fastestLap",
                   "RANK": "rank",
                   "FASTEST_LAP_TIME": "fastestLapTime",
                   "FASTEST_LAP_SPEED": "fastestLapSpeed",
                   "STATUS_ID": "statusId"}

TABLES_NAMES = {"DRIVER_STANDINGS": "driver_standings",
                "LAPTIMES": "lap_times",
                "PITSTOPS": "pit_stops",
                "RACES": "races",
                "DRIVERS": "drivers",
                "QUALIFYING": "qualifying",
                "CIRCUITS": "circuits",
                "SEASONS": "seasons",
                "RESULTS": "results",
                "STATUS": "status",
                "CONSTRUCTORS": "constructors",
                "CONSTRUCTOR_STANDINGS": "constructor_standings",
                "CONSTRUCTOR_RESULTS": "constructor_results",
                "JOINED": "joined"}
