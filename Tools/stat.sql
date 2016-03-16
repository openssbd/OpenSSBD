create or replace function genstats(startn int, endn int) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
   for i in startn..endn loop
     RAISE NOTICE 'Beginning to insert stats % into SSBD', i;
     perform genstats(i);
     	RAISE NOTICE 'Returing stats % into SSBD', i;
     count := count +1;
   end loop;
   return count;
end;
$$ language 'plpgsql';

create or replace function genstats(startn int) returns int as
$$
declare count integer:=0;
begin
     RAISE NOTICE 'Starting to insert stats % into SSBD', startn;
-- To generate only data from bdml_id=startn
INSERT into "BDML_stats_model" (bdml_id, info_id, max_x, min_x, avg_x, max_y, min_y, avg_y, max_z, min_z, avg_z, max_t, min_t, max_tp, min_tp, num_entities, num_components)
SELECT A.bdml_id as bdml_id,
B.id as info_id,
max(x) as max_x,
min(x) as min_x,
avg(x) as avg_x,
max(y) as max_y,
min(y) as min_y,
avg(y) as avg_y,
max(z) as max_z,
min(z) as min_z,
avg(z) as avg_z,
max(t) as max_t,
min(t) as min_t,
max(timept) as max_tp,
min(timept) as min_tp, 
0 as num_entities,
0 as num_components
from "BDML_unicoords_model" A INNER JOIN "BDML_info_model" B on A.bdml_id=B.bdml_id
where A.bdml_id=startn group by A.bdml_id, B.id;
	RAISE NOTICE 'Inserted stats % into SSBD', startn;
	count := count +1;
  return count;
end;
$$ language 'plpgsql'
-- Bash usage:  for ((i=1; i<100; i++)); do /opt/local/bin/psql92 -U postgres -h host -d "database" -c "select genstats($i)"; done