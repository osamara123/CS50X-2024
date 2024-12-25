-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get description
SELECT description FROM crime_scene_reports
WHERE day = 28 AND year = 2021 AND month = 7 AND street = 'Humphrey Street';

-- Get transcipts mentioning bakery
SELECT transcript FROM interviews
WHERE day = 28 AND year = 2021 AND month = 7 AND transcript LIKE '%bakery%';

-- Suspect of all names from people through the info of witness 3
SELECT DISTINCT(name), phone_calls.caller FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE phone_calls.year = 2021 AND phone_calls.day = 28 AND phone_calls.month = 7 AND phone_calls.duration < 60;

-- continue witness 3

SELECt DISTINCT(people.name), flights.hour, flights.minute, flights.destination_airport_id FROM people JOIN passengers ON passengers.passport_number = people.passport_number
JOIN flights ON flights.id = passengers.flight_id JOIN airports ON airports.id = flights.origin_airport_id
WHERE airports.city = 'Fiftyville' AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29 ORDER BY flights.hour, flights.minute;

-- common names of the two results considering only the first flights out of fityville at 8:20 are Sofia, Kelsey, Bruce, Taylor, Kenny

-- Suspect of all the names from info of witness 2 and find common names
SELECT name FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw';

-- Common names are Bruce , Taylor, Kenny

-- get all names from people from info of witness 1, compare with list of names before
SELECT name FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10 AND bakery_security_logs. minute >= 15 AND bakery_security_logs.minute <= 25 AND bakery_security_logs.activity = 'exit';

-- After checking the common name, Bruce must be the theif.

-- getting destination of the theif and reciever's name.

SELECT name from people JOIN phone_calls ON phone_calls.receiver = people.phone_number
WHERE phone_calls.caller = '(367) 555-5533' AND phone_calls.year = 2021 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration < 60;

-- Robin is the accomplice

SELECT DISTINCT(city) FROM airports JOIN flights ON airports.id = flights.destination_airport_id WHERE flights.destination_airport_id = 4;

-- destination is NEW York City