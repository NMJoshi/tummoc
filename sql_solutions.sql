-- 1
select rp.route_id,r."name", sum(rp.distance) as total_distance  from route_points rp left join route r on r.id=rp.route_id  group by route_id,r."name";

-- 2
select distinct(rp.route_id),
(select  min(stop_id)  from route_points where route_id = r.id) as source_stop_id,
(select  max(stop_id)  from route_points where route_id = r.id) as dest_stop_id
from route r 
left join route_points rp on r.id = rp.route_id;


-- 3
select t.station_id,s.name as station_name,t.slot,t.time from station s  left join times t on s.id=t.station_id where t."time"<='6:40';