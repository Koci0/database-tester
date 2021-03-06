create table status
(
    "statusId" integer not null
        constraint status_pk
            primary key,
    status     text
);

alter table status
    owner to root;

INSERT INTO public.status ("statusId", status) VALUES (1, 'Finished');
INSERT INTO public.status ("statusId", status) VALUES (2, 'Disqualified');
INSERT INTO public.status ("statusId", status) VALUES (3, 'Accident');
INSERT INTO public.status ("statusId", status) VALUES (4, 'Collision');
INSERT INTO public.status ("statusId", status) VALUES (5, 'Engine');
INSERT INTO public.status ("statusId", status) VALUES (6, 'Gearbox');
INSERT INTO public.status ("statusId", status) VALUES (7, 'Transmission');
INSERT INTO public.status ("statusId", status) VALUES (8, 'Clutch');
INSERT INTO public.status ("statusId", status) VALUES (9, 'Hydraulics');
INSERT INTO public.status ("statusId", status) VALUES (10, 'Electrical');
INSERT INTO public.status ("statusId", status) VALUES (11, '+1 Lap');
INSERT INTO public.status ("statusId", status) VALUES (12, '+2 Laps');
INSERT INTO public.status ("statusId", status) VALUES (13, '+3 Laps');
INSERT INTO public.status ("statusId", status) VALUES (14, '+4 Laps');
INSERT INTO public.status ("statusId", status) VALUES (15, '+5 Laps');
INSERT INTO public.status ("statusId", status) VALUES (16, '+6 Laps');
INSERT INTO public.status ("statusId", status) VALUES (17, '+7 Laps');
INSERT INTO public.status ("statusId", status) VALUES (18, '+8 Laps');
INSERT INTO public.status ("statusId", status) VALUES (19, '+9 Laps');
INSERT INTO public.status ("statusId", status) VALUES (20, 'Spun off');
INSERT INTO public.status ("statusId", status) VALUES (21, 'Radiator');
INSERT INTO public.status ("statusId", status) VALUES (22, 'Suspension');
INSERT INTO public.status ("statusId", status) VALUES (23, 'Brakes');
INSERT INTO public.status ("statusId", status) VALUES (24, 'Differential');
INSERT INTO public.status ("statusId", status) VALUES (25, 'Overheating');
INSERT INTO public.status ("statusId", status) VALUES (26, 'Mechanical');
INSERT INTO public.status ("statusId", status) VALUES (27, 'Tyre');
INSERT INTO public.status ("statusId", status) VALUES (28, 'Driver Seat');
INSERT INTO public.status ("statusId", status) VALUES (29, 'Puncture');
INSERT INTO public.status ("statusId", status) VALUES (30, 'Driveshaft');
INSERT INTO public.status ("statusId", status) VALUES (31, 'Retired');
INSERT INTO public.status ("statusId", status) VALUES (32, 'Fuel pressure');
INSERT INTO public.status ("statusId", status) VALUES (33, 'Front wing');
INSERT INTO public.status ("statusId", status) VALUES (34, 'Water pressure');
INSERT INTO public.status ("statusId", status) VALUES (35, 'Refuelling');
INSERT INTO public.status ("statusId", status) VALUES (36, 'Wheel');
INSERT INTO public.status ("statusId", status) VALUES (37, 'Throttle');
INSERT INTO public.status ("statusId", status) VALUES (38, 'Steering');
INSERT INTO public.status ("statusId", status) VALUES (39, 'Technical');
INSERT INTO public.status ("statusId", status) VALUES (40, 'Electronics');
INSERT INTO public.status ("statusId", status) VALUES (41, 'Broken wing');
INSERT INTO public.status ("statusId", status) VALUES (42, 'Heat shield fire');
INSERT INTO public.status ("statusId", status) VALUES (43, 'Exhaust');
INSERT INTO public.status ("statusId", status) VALUES (44, 'Oil leak');
INSERT INTO public.status ("statusId", status) VALUES (45, '+11 Laps');
INSERT INTO public.status ("statusId", status) VALUES (46, 'Wheel rim');
INSERT INTO public.status ("statusId", status) VALUES (47, 'Water leak');
INSERT INTO public.status ("statusId", status) VALUES (48, 'Fuel pump');
INSERT INTO public.status ("statusId", status) VALUES (49, 'Track rod');
INSERT INTO public.status ("statusId", status) VALUES (50, '+17 Laps');
INSERT INTO public.status ("statusId", status) VALUES (51, 'Oil pressure');
INSERT INTO public.status ("statusId", status) VALUES (53, '+13 Laps');
INSERT INTO public.status ("statusId", status) VALUES (54, 'Withdrew');
INSERT INTO public.status ("statusId", status) VALUES (55, '+12 Laps');
INSERT INTO public.status ("statusId", status) VALUES (56, 'Engine fire');
INSERT INTO public.status ("statusId", status) VALUES (58, '+26 Laps');
INSERT INTO public.status ("statusId", status) VALUES (59, 'Tyre puncture');
INSERT INTO public.status ("statusId", status) VALUES (60, 'Out of fuel');
INSERT INTO public.status ("statusId", status) VALUES (61, 'Wheel nut');
INSERT INTO public.status ("statusId", status) VALUES (62, 'Not classified');
INSERT INTO public.status ("statusId", status) VALUES (63, 'Pneumatics');
INSERT INTO public.status ("statusId", status) VALUES (64, 'Handling');
INSERT INTO public.status ("statusId", status) VALUES (65, 'Rear wing');
INSERT INTO public.status ("statusId", status) VALUES (66, 'Fire');
INSERT INTO public.status ("statusId", status) VALUES (67, 'Wheel bearing');
INSERT INTO public.status ("statusId", status) VALUES (68, 'Physical');
INSERT INTO public.status ("statusId", status) VALUES (69, 'Fuel system');
INSERT INTO public.status ("statusId", status) VALUES (70, 'Oil line');
INSERT INTO public.status ("statusId", status) VALUES (71, 'Fuel rig');
INSERT INTO public.status ("statusId", status) VALUES (72, 'Launch control');
INSERT INTO public.status ("statusId", status) VALUES (73, 'Injured');
INSERT INTO public.status ("statusId", status) VALUES (74, 'Fuel');
INSERT INTO public.status ("statusId", status) VALUES (75, 'Power loss');
INSERT INTO public.status ("statusId", status) VALUES (76, 'Vibrations');
INSERT INTO public.status ("statusId", status) VALUES (77, '107% Rule');
INSERT INTO public.status ("statusId", status) VALUES (78, 'Safety');
INSERT INTO public.status ("statusId", status) VALUES (79, 'Drivetrain');
INSERT INTO public.status ("statusId", status) VALUES (80, 'Ignition');
INSERT INTO public.status ("statusId", status) VALUES (81, 'Did not qualify');
INSERT INTO public.status ("statusId", status) VALUES (82, 'Injury');
INSERT INTO public.status ("statusId", status) VALUES (83, 'Chassis');
INSERT INTO public.status ("statusId", status) VALUES (84, 'Battery');
INSERT INTO public.status ("statusId", status) VALUES (85, 'Stalled');
INSERT INTO public.status ("statusId", status) VALUES (86, 'Halfshaft');
INSERT INTO public.status ("statusId", status) VALUES (87, 'Crankshaft');
INSERT INTO public.status ("statusId", status) VALUES (88, '+10 Laps');
INSERT INTO public.status ("statusId", status) VALUES (89, 'Safety concerns');
INSERT INTO public.status ("statusId", status) VALUES (90, 'Not restarted');
INSERT INTO public.status ("statusId", status) VALUES (91, 'Alternator');
INSERT INTO public.status ("statusId", status) VALUES (92, 'Underweight');
INSERT INTO public.status ("statusId", status) VALUES (93, 'Safety belt');
INSERT INTO public.status ("statusId", status) VALUES (94, 'Oil pump');
INSERT INTO public.status ("statusId", status) VALUES (95, 'Fuel leak');
INSERT INTO public.status ("statusId", status) VALUES (96, 'Excluded');
INSERT INTO public.status ("statusId", status) VALUES (97, 'Did not prequalify');
INSERT INTO public.status ("statusId", status) VALUES (98, 'Injection');
INSERT INTO public.status ("statusId", status) VALUES (99, 'Distributor');
INSERT INTO public.status ("statusId", status) VALUES (100, 'Driver unwell');
INSERT INTO public.status ("statusId", status) VALUES (101, 'Turbo');
INSERT INTO public.status ("statusId", status) VALUES (102, 'CV joint');
INSERT INTO public.status ("statusId", status) VALUES (103, 'Water pump');
INSERT INTO public.status ("statusId", status) VALUES (104, 'Fatal accident');
INSERT INTO public.status ("statusId", status) VALUES (105, 'Spark plugs');
INSERT INTO public.status ("statusId", status) VALUES (106, 'Fuel pipe');
INSERT INTO public.status ("statusId", status) VALUES (107, 'Eye injury');
INSERT INTO public.status ("statusId", status) VALUES (108, 'Oil pipe');
INSERT INTO public.status ("statusId", status) VALUES (109, 'Axle');
INSERT INTO public.status ("statusId", status) VALUES (110, 'Water pipe');
INSERT INTO public.status ("statusId", status) VALUES (111, '+14 Laps');
INSERT INTO public.status ("statusId", status) VALUES (112, '+15 Laps');
INSERT INTO public.status ("statusId", status) VALUES (113, '+25 Laps');
INSERT INTO public.status ("statusId", status) VALUES (114, '+18 Laps');
INSERT INTO public.status ("statusId", status) VALUES (115, '+22 Laps');
INSERT INTO public.status ("statusId", status) VALUES (116, '+16 Laps');
INSERT INTO public.status ("statusId", status) VALUES (117, '+24 Laps');
INSERT INTO public.status ("statusId", status) VALUES (118, '+29 Laps');
INSERT INTO public.status ("statusId", status) VALUES (119, '+23 Laps');
INSERT INTO public.status ("statusId", status) VALUES (120, '+21 Laps');
INSERT INTO public.status ("statusId", status) VALUES (121, 'Magneto');
INSERT INTO public.status ("statusId", status) VALUES (122, '+44 Laps');
INSERT INTO public.status ("statusId", status) VALUES (123, '+30 Laps');
INSERT INTO public.status ("statusId", status) VALUES (124, '+19 Laps');
INSERT INTO public.status ("statusId", status) VALUES (125, '+46 Laps');
INSERT INTO public.status ("statusId", status) VALUES (126, 'Supercharger');
INSERT INTO public.status ("statusId", status) VALUES (127, '+20 Laps');
INSERT INTO public.status ("statusId", status) VALUES (128, '+42 Laps');
INSERT INTO public.status ("statusId", status) VALUES (129, 'Engine misfire');
INSERT INTO public.status ("statusId", status) VALUES (130, 'Collision damage');
INSERT INTO public.status ("statusId", status) VALUES (131, 'Power Unit');
INSERT INTO public.status ("statusId", status) VALUES (132, 'ERS');
INSERT INTO public.status ("statusId", status) VALUES (133, '+49 Laps');
INSERT INTO public.status ("statusId", status) VALUES (134, '+38 Laps');
INSERT INTO public.status ("statusId", status) VALUES (135, 'Brake duct');
INSERT INTO public.status ("statusId", status) VALUES (136, 'Seat');
