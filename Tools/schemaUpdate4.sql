create or replace function schemaupdate4(bdmlid int) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
    insert into "SSBD2_meta_data_model"
    (name, "E_mail", phone, "URL", organization, department, laboratory, address, title, description, organism, datatype, localid, basedon, contributors, citation, "PMID", dblink, license, "method_summary", orf, gene, oldbdmlid)
    select
        D.name,
        D."E_mail",
        D.phone,
        D."URL",
        D.organization,
        D.department,
        D.laboratory,
        D.address,
        A.title,
        C.description,
        C.organism,
        C.datatype,
        C.identifier as localid,
        C.basedon,
        C.contributors,
        C.citation,
        C."PMID",
        C.dblink,
        B.license,
        E.summary as "method_summary",
        NULL as orf,
        NULL as gene,
        A.id as oldbdmlid
    from "BDML_bdml_model" A
    INNER JOIN "BDML_info_model" B on A.id=B.bdml_id
    INNER JOIN "BDML_summary_model" C ON C.bdml_id=A.id
    INNER JOIN "BDML_contact_model" D ON D.bdml_id=A.id
    INNER JOIN "BDML_methods_model" E ON E.bdml_id=A.id
    where A.id = bdmlid;
    RAISE NOTICE 'Inserted % into SSBD2_meta_data_model', bdmlid;
    insert into "SSBD2_quant_data_model" (localid, oldbdmlid)
    select
      identifier as localid,
      "bdml_id" as oldbdmlid
    from "BDML_summary_model" A
    where A.id = bdmlid;
    RAISE NOTICE 'Inserted % into SSBD2_quant_data_model', bdmlid;
    insert into "SSBD2_scaleunit_model" ("quant_data_id", "xScale", "yScale", "zScale", "xyzUnit", "tScale", "tUnit")
    select
      A."bdml_id" as "quant_data_id",
      "xScale",
      "yScale",
      "zScale",
      "xyzUnit",
      "tScale",
      "tUnit"
    from "BDML_scaleunit_model" A
    where A."bdml_id" = bdmlid;
    RAISE NOTICE 'Inserted % into SSBD2_scaleunit_data_model', bdmlid;
    insert into "SSBD2_bdml_multipart_model"
    ("bdmlUUID",
        localid,
        type,
        oldbdmlid
    )
    select
        B."bdmlID" as "bdmlUUID",
        A.identifier as localid,
        1 as type,
        bdmlid as oldbdmlid
    from "BDML_summary_model" A
    INNER JOIN "BDML_info_model" B on A."bdml_id"=B."bdml_id"
    where A."bdml_id" = bdmlid;
    RAISE NOTICE 'Inserted % into SSBD2_bml_multipart_model', bdmlid;
    insert into "SSBD2_root_model" (
        "bdml_multipart_id",
        "bdml_multipart_type",
        "meta_data_id",
        "quant_data_id",
        "scaleunit_id",
        "omero_datasetID",
        "owner_id",
        "schema_ver",
        "bdmlUUID",
        localid,
        release,
        status,
        "external_bdml",
        "external_pdpml",
        "external_source",
        "internal_bdml",
        "internal_pdpml",
        "internal_source")
    select
        C.id as "bdml_mulipart_id",
        C.type as "bdml_multipart_type",
        D.id as "meta_data_id",
        B.id as "quant_data_id",
        H.id as "scaleunit_id",
        NULL as "omero_datasetID",
        1 as "owner_id",
        '0.15' as "schema_ver",
        C."bdmlUUID",
        E.identifier as localid,
        F.release,
        'available' as status,
        NULL as "external_bdml",
        NULL as "external_pdpml",
        NULL as "external_source",
        NULL as "internal_bdml",
        NULL as "internal_pdpml",
        NULL as "internal_source"
    from "BDML_bdml_model" A
    LEFT OUTER JOIN "SSBD2_quant_data_model" B on A.id=B.oldbdmlid
    LEFT OUTER JOIN "SSBD2_bdml_multipart_model" C on A."bdml_ID"=C."bdmlUUID"
    LEFT OUTER JOIN "SSBD2_meta_data_model" D on A.id=D.oldbdmlid
    LEFT OUTER JOIN "BDML_summary_model" E on A.id=E."bdml_id"
    LEFT OUTER JOIN "BDML_info_model" F on A.id=F."bdml_id"
    LEFT OUTER JOIN "SSBD2_scaleunit_model" H on H."quant_data_id"=A.id
    where A.id = bdmlid;
    RAISE NOTICE 'Inserted % into SSBD2_root_data_model', bdmlid;
		count := count +1;
	return count;
end;
$$ language 'plpgsql';

create or replace function schemaupdate(startn int, endn int, new_version int, schema_ver real, status_txt text) returns int as
$$
declare
	i int;
declare count integer:=0;
begin
	for i in startn..endn loop
			insert into "BDML_update_model" (ssbd_id, data_id, version, "schema", "bdmlUUID", localid, source, pdpml, status )
                select (split_part(B.contributors,',',1)||'_'||A.bdml_id) as ssbd_id, A.bdml_id as data_id, new_version, schema_ver as "schema", A."bdmlID" as bdmlUUID, B.identifier as localID, C.source, C.pdpml, status_txt as status
                      from "BDML_info_model" A
                      INNER JOIN "BDML_summary_model" B on A.bdml_id=B.bdml_id
                      INNER JOIN "BDML_methods_model" C on A.bdml_id=C.bdml_id
                where A.bdml_id = i;
		count := count +1;
	end loop;
	return count;
end;
$$ language 'plpgsql';

