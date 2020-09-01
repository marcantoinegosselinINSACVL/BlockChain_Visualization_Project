import os
import json

if __name__ == "__main__":
    params = ' -u kibanaadmin:azerty -H \'kbn-version: 7.6.1\' '
    url = "'http://172.30.10.12/api/reporting/generate/csv?jobParams=(conflictedTypesFields:!(),fields:!(%27@timestamp%27,%27@version%27,_id,_index,_score,_type,agent.ephemeral_id,agent.hostname,agent.id,agent.type,agent.version,block-hash,block-timestamp,date-mine,ecs.version,filename,height,host.name,input.type,log.file.path,log.offset,message,recv-date,recv-time,recv-timestamp,suricata.eve.timestamp,tags,tx,work),indexPatternId:%272e334dc0-7020-11ea-a1dd-6d4e11bb6207%27,metaFields:!(_source,_id,_type,_index,_score),searchRequest:(body:(_source:(excludes:!()),docvalue_fields:!((field:%27@timestamp%27,format:date_time),(field:aws.cloudtrail.user_identity.session_context.creation_date,format:date_time),(field:azure.auditlogs.properties.activity_datetime,format:date_time),(field:azure.enqueued_time,format:date_time),(field:azure.signinlogs.properties.created_at,format:date_time),(field:cef.extensions.agentReceiptTime,format:date_time),(field:cef.extensions.deviceCustomDate1,format:date_time),(field:cef.extensions.deviceCustomDate2,format:date_time),(field:cef.extensions.deviceReceiptTime,format:date_time),(field:cef.extensions.endTime,format:date_time),(field:cef.extensions.fileCreateTime,format:date_time),(field:cef.extensions.fileModificationTime,format:date_time),(field:cef.extensions.flexDate1,format:date_time),(field:cef.extensions.managerReceiptTime,format:date_time),(field:cef.extensions.oldFileCreateTime,format:date_time),(field:cef.extensions.oldFileModificationTime,format:date_time),(field:cef.extensions.startTime,format:date_time),(field:event.created,format:date_time),(field:event.end,format:date_time),(field:event.ingested,format:date_time),(field:event.start,format:date_time),(field:file.accessed,format:date_time),(field:file.created,format:date_time),(field:file.ctime,format:date_time),(field:file.mtime,format:date_time),(field:kafka.block_timestamp,format:date_time),(field:misp.campaign.first_seen,format:date_time),(field:misp.campaign.last_seen,format:date_time),(field:misp.intrusion_set.first_seen,format:date_time),(field:misp.intrusion_set.last_seen,format:date_time),(field:misp.observed_data.first_observed,format:date_time),(field:misp.observed_data.last_observed,format:date_time),(field:misp.report.published,format:date_time),(field:misp.threat_indicator.valid_from,format:date_time),(field:misp.threat_indicator.valid_until,format:date_time),(field:netflow.collection_time_milliseconds,format:date_time),(field:netflow.exporter.timestamp,format:date_time),(field:netflow.flow_end_microseconds,format:date_time),(field:netflow.flow_end_milliseconds,format:date_time),(field:netflow.flow_end_nanoseconds,format:date_time),(field:netflow.flow_end_seconds,format:date_time),(field:netflow.flow_start_microseconds,format:date_time),(field:netflow.flow_start_milliseconds,format:date_time),(field:netflow.flow_start_nanoseconds,format:date_time),(field:netflow.flow_start_seconds,format:date_time),(field:netflow.max_export_seconds,format:date_time),(field:netflow.max_flow_end_microseconds,format:date_time),(field:netflow.max_flow_end_milliseconds,format:date_time),(field:netflow.max_flow_end_nanoseconds,format:date_time),(field:netflow.max_flow_end_seconds,format:date_time),(field:netflow.min_export_seconds,format:date_time),(field:netflow.min_flow_start_microseconds,format:date_time),(field:netflow.min_flow_start_milliseconds,format:date_time),(field:netflow.min_flow_start_nanoseconds,format:date_time),(field:netflow.min_flow_start_seconds,format:date_time),(field:netflow.monitoring_interval_end_milli_seconds,format:date_time),(field:netflow.monitoring_interval_start_milli_seconds,format:date_time),(field:netflow.observation_time_microseconds,format:date_time),(field:netflow.observation_time_milliseconds,format:date_time),(field:netflow.observation_time_nanoseconds,format:date_time),(field:netflow.observation_time_seconds,format:date_time),(field:netflow.system_init_time_milliseconds,format:date_time),(field:package.installed,format:date_time),(field:process.parent.start,format:date_time),(field:process.start,format:date_time),(field:suricata.eve.flow.end,format:date_time),(field:suricata.eve.flow.start,format:date_time),(field:suricata.eve.timestamp,format:date_time),(field:suricata.eve.tls.notafter,format:date_time),(field:suricata.eve.tls.notbefore,format:date_time),(field:tls.client.not_after,format:date_time),(field:tls.client.not_before,format:date_time),(field:tls.server.not_after,format:date_time),(field:tls.server.not_before,format:date_time),(field:zeek.kerberos.valid.from,format:date_time),(field:zeek.kerberos.valid.until,format:date_time),(field:zeek.ocsp.revoke.time,format:date_time),(field:zeek.ocsp.update.next,format:date_time),(field:zeek.ocsp.update.this,format:date_time),(field:zeek.pe.compile_time,format:date_time),(field:zeek.smb_files.times.accessed,format:date_time),(field:zeek.smb_files.times.changed,format:date_time),(field:zeek.smb_files.times.created,format:date_time),(field:zeek.smb_files.times.modified,format:date_time),(field:zeek.smtp.date,format:date_time),(field:zeek.snmp.up_since,format:date_time),(field:zeek.x509.certificate.valid.from,format:date_time),(field:zeek.x509.certificate.valid.until,format:date_time)),query:(bool:(filter:!((match_all:()),(range:(log.offset:(gte:23100000,lt:23200000))),(range:(%27@timestamp%27:(format:strict_date_optional_time,gte:%272020-09-01T03:58:51.063Z%27,lte:%272020-09-01T06:58:51.063Z%27)))),must:!(),must_not:!(),should:!())),script_fields:(),sort:!((%27@timestamp%27:(order:desc,unmapped_type:boolean))),stored_fields:!(%27*%27),version:!t),index:%27filebeat*%27),title:%2731%2F08%2F2020%27,type:search)'"
    myCmd = os.popen('curl -X POST' + params + url).read()
    url = '\'http://172.30.10.12:5601/' + json.loads(myCmd)['path'] + '\''
    print(url)
    myCmd = os.system('curl -X GET' + params + url)