# Week 3

## Exercises 2: Single Table Queries

### Question 1:
select * from goal;

![Screenshot 2024-09-12 151240.png](Screenshot%202024-09-12%20151240.png)

### Question 2:
select name, type from airport where iso_country = "FI";

![Screenshot 2024-09-12 152911.png](Screenshot%202024-09-12%20152911.png)

### Question 3:
select name from airport where iso_country = "FI" order by name;

![Screenshot 2024-09-12 153535.png](Screenshot%202024-09-12%20153535.png)

### Question 4:
select name, type from airport where iso_country = "FI" order by type, name;

![Screenshot 2024-09-12 171058.png](Screenshot%202024-09-12%20171058.png)

### Question 5:
select name from country where name like "F%";

![Screenshot 2024-09-12 171449.png](Screenshot%202024-09-12%20171449.png)

### Question 6:
select name from country where name like "%F%";

![Screenshot 2024-09-12 171709.png](Screenshot%202024-09-12%20171709.png)

### Question 7
select location from game where screen_name = "Vesa";

![Screenshot 2024-09-12 172044.png](Screenshot%202024-09-12%20172044.png)

### Question 8:
select co2_consumed from game where screen_name = "Ilkka";

![Screenshot 2024-09-12 172642.png](Screenshot%202024-09-12%20172642.png)

### Question 9:
select distinct co2_budget from game;

![Screenshot 2024-09-12 172828.png](Screenshot%202024-09-12%20172828.png)

### Question 10:
select screen_name, co2_budget, co2_consumed, co2_budget - co2_consumed as co2_left from game where screen_name = "Ilkka";

![Screenshot 2024-09-12 173650.png](Screenshot%202024-09-12%20173650.png)

## Exercises 3: Multiple Table Queries

### Question 1:
select country.name as "country name", airport.name as "airport name" from airport, country where airport.iso_country = country.iso_country and country.name = "Iceland";

![Screenshot 2024-09-12 214817.png](Screenshot%202024-09-12%20214817.png)

### Question 2:
select airport.name as "airport name" from airport, country where airport.iso_country = country.iso_country and country.name = "France" and airport.type = "large_airport";

![Screenshot 2024-09-12 215514.png](Screenshot%202024-09-12%20215514.png)

### Question 3:
select country.name as country_name, airport.name as airport_name from airport, country where airport.iso_country = country.iso_country and country.continent = "an";

![Screenshot 2024-09-12 220131.png](Screenshot%202024-09-12%20220131.png)

### Question 4:
select elevation_ft from airport, game where location = ident and screen_name = "Heini";

![Screenshot 2024-09-12 220555.png](Screenshot%202024-09-12%20220555.png)

### Question 5:
select elevation_ft * 0.3048 as elevation_m from airport, game where location = ident and screen_name = "Heini";

![Screenshot 2024-09-12 221036.png](Screenshot%202024-09-12%20221036.png)

### Question 6:
select name from airport, game where location = ident and screen_name = "Ilkka";

![Screenshot 2024-09-12 221325.png](Screenshot%202024-09-12%20221325.png)

### Question 7:
select country.name from airport, country, game where airport.iso_country = country.iso_country and location = ident and screen_name = "Ilkka";

![Screenshot 2024-09-12 221808.png](Screenshot%202024-09-12%20221808.png)

### Question 8:
select name from goal, goal_reached, game where game.id = game_id and goal.id = goal_id and screen_name = "Heini";

![Screenshot 2024-09-12 222256.png](Screenshot%202024-09-12%20222256.png)

### Question 9:
select airport.name from airport, game, goal, goal_reached where ident = location and game.id = game_id and goal.id = goal_id and screen_name = "Ilkka" and goal.name = "CLOUDS";

![Screenshot 2024-09-12 222716.png](Screenshot%202024-09-12%20222716.png)

### Question 10:
select country.name from country, airport, game, goal, goal_reached where airport.iso_country = country.iso_country and ident = location and game.id = game_id and goal.id = goal_id and screen_name = "Ilkka" and goal.name = "CLOUDS";

![Screenshot 2024-09-12 214023.png](Screenshot%202024-09-12%20214023.png)

