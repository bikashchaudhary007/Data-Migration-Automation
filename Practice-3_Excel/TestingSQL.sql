use NexGenCoSysDBDev
go

select * from MemMemberRegistration;

--delete from MemMemberRegistration
--dbcc checkident('MemMemberRegistration',reseed,0)