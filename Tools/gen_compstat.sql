create or replace function gen_compstat(startn int, endn int) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
   for i in startn..endn loop
     RAISE NOTICE 'Beginning to insert comp_stats % into SSBD', i;
     perform gen_compstat(i);
     	RAISE NOTICE 'Returning comp_stats % into SSBD', i;
     count := count +1;
   end loop;
   return count;
end;
$$ language 'plpgsql';

create or replace function gen_compstat(startbdml int) returns int as
$$
declare count integer:=0;
begin
    RAISE NOTICE 'Starting to insert comp_stats % into SSBD', startbdml;
		insert into "BDML_compstats_model" (bdml_id, max_x, min_x, avg_x, max_y, min_y, avg_y, max_z, min_z, avg_z, measurement_id, component_id,  t, tp)
                select bdml_id, max(x), min(x), avg(x), max(y), min(y), avg(y), max(z), min(z), avg(z), measurement_id, component_id, t, timept as tp
                    from "BDML_unicoords_model"
                          where bdml_id=startbdml group by component_id, measurement_id, t, timept, bdml_id order by timept, t, measurement_id, component_id ;
    RAISE NOTICE 'Inserted stats % into SSBD', startbdml;
	  count := count +1;
	  return count;
end;
$$ language 'plpgsql';

create or replace function gen_compstat(startn int, endn int) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
	for i in startn..endn loop
		insert into "BDML_compstats_model" (bdml_id, max_x, min_x, avg_x, max_y, min_y, avg_y, max_z, min_z, avg_z, measurement_id, component_id,  t)
                select bdml_id, max(x), min(x), avg(x), max(y), min(y), avg(y), max(z), min(z), avg(z), measurement_id, component_id, t
                    from "BDML_unicoords_model"
                          where bdml_id=i group by component_id, measurement_id, t, bdml_id order by t, measurement_id, component_id ;
		count := count +1;
	end loop;
	return count;
end;
$$ language 'plpgsql';