CREATE OR REPLACE FUNCTION unicoords(startn integer, unit text, tunit text, scale real, tscale real) RETURNS integer AS
$$
declare count integer:=0;
begin
				insert into "BDML_unicoords_model" (
                                 coords_id, bdml_id, x, y, z, t, radius, entitytype, entity_id,
                                 measurement_id, component_id, info_id, summary_id)
                select A.id as coords_id,
                   A.bdml_id,
                   A.x * B."xScale" * scale as x,
                   A.y * B."yScale" * scale as y,
                   A.z * B."zScale" * scale as z,
                   A.t * B."tScale" * tscale as t,
                   A.radius,
                   A.entitytype,
                   A.entity_id,
                   E.measurement_id as measurement_id,
                   E.component_id as component_id,
                   C.id as info_id,
                   D.id as summary_id
                FROM "BDML_coordinates_model" A
                                        INNER JOIN "BDML_scaleunit_model" B ON A.bdml_id=B.bdml_id
                                        INNER JOIN "BDML_info_model" C ON C.bdml_id=A.bdml_id
                                        INNER JOIN "BDML_summary_model" D ON D.bdml_id=A.bdml_id
                                        INNER JOIN "BDML_entity_model" E ON E.id=A.entity_id
                             where A.bdml_id=startn and B."xyzUnit"=unit and B."tUnit"=tunit;
		count := count +1;
	return count;
end;
$$ language 'plpgsql';

create or replace function unicoords(startn int, endn int, unit text, tunit text, scale real, tscale real) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
	for i in startn..endn loop
		insert into "BDML_unicoords_model" (
                                 coords_id, bdml_id, x, y, z, t, radius, entitytype, entity_id,
                                 measurement_id, component_id, info_id, summary_id)
                select A.id as coords_id,
                   A.bdml_id,
                   A.x * B."xScale" * scale as x,
                   A.y * B."yScale" * scale as y,
                   A.z * B."zScale" * scale as z,
                   A.t * B."tScale" * tscale as t,
                   A.radius,
                   A.entitytype,
                   A.entity_id,
                   E.measurement_id as measurement_id,
                   E.component_id as component_id,
                   C.id as info_id,
                   D.id as summary_id
                FROM "BDML_coordinates_model" A
                                        INNER JOIN "BDML_scaleunit_model" B ON A.bdml_id=B.bdml_id
                                        INNER JOIN "BDML_info_model" C ON C.bdml_id=A.bdml_id
                                        INNER JOIN "BDML_summary_model" D ON D.bdml_id=A.bdml_id
                                        INNER JOIN "BDML_entity_model" E ON E.id=A.entity_id
                             where A.bdml_id=i and B."xyzUnit"=unit and B."tUnit"=tunit;
		count := count +1;
	end loop;
	return count;
end;
$$ language 'plpgsql';

create or replace function unicoords1(startn int, endn int) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
	for i in startn..endn loop
	  RAISE NOTICE 'Starting to insert % into SSBD', i;
		insert into "BDML_unicoords1_model" (
                                 coords_id, bdml_id, x, y, z, t, timept, radius, entitytype, entity_id,
                                 measurement_id, component_id, info_id, summary_id)
                select A.coords_id, A.bdml_id, A.x, A.y, A.z, A.t, B.time as timept, A.radius, A.entitytype, A.entity_id,
                       A.measurement_id, A.component_id, A.summary_id, A.info_id
                FROM "BDML_unicoords_model" A INNER JOIN "BDML_component_model" B on A.component_id=B.id
                      where A.bdml_id=i;
    RAISE NOTICE 'Inserted % into SSBD', i;
		count := count +1;
	end loop;
	return count;
end;
$$ language 'plpgsql';

create or replace function unicoords1(i int) returns int as
$$
declare count integer:=0;
begin
	  RAISE NOTICE 'Starting to insert % into SSBD', i;
		insert into "BDML_unicoords1_model" (
                                 coords_id, bdml_id, x, y, z, t, timept, radius, entitytype, entity_id,
                                 measurement_id, component_id, info_id, summary_id)
                select A.coords_id, A.bdml_id, A.x, A.y, A.z, A.t, B.time as timept, A.radius, A.entitytype, A.entity_id,
                       A.measurement_id, A.component_id, A.summary_id, A.info_id
                FROM "BDML_unicoords_model" A INNER JOIN "BDML_component_model" B on A.component_id=B.id
                      where A.bdml_id=i;
    RAISE NOTICE 'Inserted % into SSBD', i;
		count := count +1;
	return count;
end;
$$ language 'plpgsql';

-- Usage Bash: for ((i=211; i<213; i++)); do /opt/local/bin/psql92 -U postgres -h so0006 -d "SSBD20140704" -c "select unicoords1($i)"; done

create or replace function unicoords(startn int, endn int) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
   for i in startn..endn loop
     RAISE NOTICE 'Starting to insert % into SSBD', i;
     insert into "BDML_unicoords_model" (
                                 coords_id, bdml_id, x, y, z, t, timept, radius, entitytype, entity_id,
                                 measurement_id, component_id, summary_id, info_id)
	select
            A.id as coords_id,
            A.bdml_id,
            A.x * B."xScale" * case when B."xyzUnit"='micrometer' then 1
                              			when B."xyzUnit"='meter' then 1000000
                              	end as x,
            A.y * B."yScale" * case when B."xyzUnit"='micrometer' then 1
                              			when B."xyzUnit"='meter' then 1000000
                              	end as y,
            A.z * B."zScale" * case when B."xyzUnit"='micrometer' then 1
                              			when B."xyzUnit"='meter' then 1000000
                              	end as z,
            A.t * B."tScale" * case when B."tUnit"='second' then 1
                              			when B."tUnit"='microsecond' then 0.000001
                              			when B."tUnit"='millisecond' then 0.001
                              			when B."tUnit"='minute' then 60
                                end as t,
            A.t as timept,
            A.radius,
            A.entitytype,
            A.entity_id,
            E.measurement_id as measurement_id,
            E.component_id as component_id,
            D.id as summary_id,
            C.id as info_id
        FROM "BDML_coordinates_model" A
              INNER JOIN "BDML_scaleunit_model" B ON A.bdml_id=B.bdml_id
              INNER JOIN "BDML_info_model" C ON C.bdml_id=A.bdml_id
              INNER JOIN "BDML_summary_model" D ON D.bdml_id=A.bdml_id
              INNER JOIN "BDML_entity_model" E ON E.id=A.entity_id
        where A.bdml_id=i;
	RAISE NOTICE 'Inserted % into SSBD', i;
	count := count +1;
   end loop;
   return count;
end;
$$ language 'plpgsql';

create or replace function unicoords(startn int) returns int as
$$
declare count integer:=0;
begin
     RAISE NOTICE 'Starting to insert % into SSBD', startn;
     insert into "BDML_unicoords_model" (
                                 coords_id, bdml_id, x, y, z, t, timept, radius, entitytype, entity_id,
                                 measurement_id, component_id, summary_id, info_id)
	      select
            A.id as coords_id,
            A.bdml_id,
            A.x * B."xScale" * case when B."xyzUnit"='micrometer' then 1
                              			when B."xyzUnit"='meter' then 1000000
                              	end as x,
            A.y * B."yScale" * case when B."xyzUnit"='micrometer' then 1
                              			when B."xyzUnit"='meter' then 1000000
                              	end as y,
            A.z * B."zScale" * case when B."xyzUnit"='micrometer' then 1
                              			when B."xyzUnit"='meter' then 1000000
                              	end as z,
            A.t * B."tScale" * case when B."tUnit"='second' then 1
                              			when B."tUnit"='microsecond' then 0.000001
                              			when B."tUnit"='millisecond' then 0.001
                              			when B."tUnit"='minute' then 60
                                end as t,
            A.t as timept,
            A.radius,
            A.entitytype,
            A.entity_id,
            E.measurement_id as measurement_id,
            E.component_id as component_id,
            D.id as summary_id,
            C.id as info_id
        FROM "BDML_coordinates_model" A
              INNER JOIN "BDML_scaleunit_model" B ON A.bdml_id=B.bdml_id
              INNER JOIN "BDML_info_model" C ON C.bdml_id=A.bdml_id
              INNER JOIN "BDML_summary_model" D ON D.bdml_id=A.bdml_id
              INNER JOIN "BDML_entity_model" E ON E.id=A.entity_id
        where A.bdml_id=startn;
	RAISE NOTICE 'Inserted % into SSBD', startn;
	count := count +1;
  return count;
end;
$$ language 'plpgsql'

-- Bash usage: for ((i=211; i<213; i++)); do /opt/local/bin/psql92 -U postgres -h host -d "database" -c "select unicoords1($i)"; done