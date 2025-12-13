-- Keep a log of any SQL queries you execute as you solve the mystery.


-- Crime scene reports
SELECT description FROM crime_scene_reports WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Interview of the witness, from the bakery
SELECT name
FROM interviews
WHERE year = 2024 AND month = 7 AND day = 28;

-- What did the witness said?
SELECT name, transcript
FROM interviews
WHERE year = 2024 AND month = 7 AND day = 28;

--  Ruth, Eugene and Raymond mentioned the thief. Mentioned: by the bakery he withdrawed some money, called someone about the flight and there might be securtiy footage from the bakery parking lot.
-- Thief withdrawing from ATM on Leggett Street on July 28, 2024.
SELECT p.name, a.transaction_type, a.amount
FROM atm_transactions a
JOIN people p ON a.account_number = p.id
WHERE a.year = 2024 AND a.month = 7 AND a.day = 28 AND a.atm_location = 'Leggett Street';

-- All ATM transaction, due to the one not working
SELECT a.atm_location, a.year, a.month, a.day, a.account_number, a.amount
FROM atm_transactions a
WHERE a.year = 2024 AND a.month = 7 AND a.day = 28;

-- The thiefs ATM machine
SELECT p.name, a.transaction_type, a.amount
FROM atm_transactions a
JOIN people p ON a.account_number = p.id
WHERE a.year = 2024
  AND a.month = 7
  AND a.day = 28
  AND a.atm_location = 'Leggett Street';

-- Transactions at the Leggett Street ATM on the day of the theft
SELECT *
FROM atm_transactions
WHERE year = 2024
   AND month = 7
   AND day = 28
   AND atm_location = 'Leggett Street';

-- What account numbers were used and who made ATM transaction on Leggett Street.
SELECT p.name, p.phone_number, p.passport_number, p.license_plate
FROM people p
JOIN bank_accounts b ON p.id = b.person_id
WHERE b.account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 86363979, 25506511, 81061156, 26013199);

-- Who of these were at the bakery?
SELECT b.license_plate, b.minute
FROM bakery_security_logs b
WHERE b.year = 2024
   AND b.month = 7
   AND b.day = 28
   AND b.activity = 'exit'
   AND b.license_plate IN ('94KL13X', 'I449449', '322W7JE', 'QX4YZN3', '30G67EN', 'L93JTIZ', '4328GD8', '1106N58', '8X428L0');

-- Phone number of the thief, extra information from Raymond's interview.
SELECT caller, receiver, duration
FROM phone_calls
WHERE year = 2024
   AND month = 7
   AND day = 28
   AND duration < 60
   AND caller IN (
      '(367) 555-5533', -- Phone number of Bruce
      '(770) 555-1861', -- Phone number of Diana
      '(829) 555-5269', -- Phone number of Iman
      '(389) 555-5198', -- Phone number of Luca
      '(286) 555-6063' -- Phone number of Taylor
   );

-- From Ruth's interview: "The thief left shortly after the theft". Earlier exit time and the caller matches = Bruce.
-- The accompliance - person who Bruce called; receiver of the call - number: (375) 555-8161.

-- The name of the accompliance.
SELECT name, phone_number
FROm people
WHERE phone_number = '(375) 555-8161';
-- Robin

-- The escape city, first destination city.
SELECT p.name, p.passport_number, a.city AS destination_city
FROM passengers ps
JOIN people p ON ps.passport_number = p.passport_number
JOIN flights f ON ps.flight_id = f.id
JOIN airports a ON f.destination_airport_id = a.id
WHERE f.year = 2024 AND f.month = 7 AND f.day = 29
ORDER BY f.hour, f.minute;
-- New York City



