---------------------------------------------------------------------------------------------------------
----------->>>>>>> 88 clientes  <<<<<< 
-----------
-----------
select *
from 
clientes_88  
select *
into clientes_88
from 
(
select distinct a.idCliente,count(b.IdPedido) numero_pedidos,sum(c.cantidad*c.preciounidad) venta_total,
sum(c.cantidad*c.preciounidad)/count(b.IdPedido) promedio_ventas
from 
clientes a inner  join pedidos b on a.idCliente=b.idCliente
            inner join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
		    inner join [dbo].[productos] d on c.idproducto=d.idproducto
group by  a.idCliente) as t1


-------------------
-------------------
select sum(venta_total)
from 
clientes_88  
select sum(venta_total)
from clientes_88
------------------------------------
------- venta total: 1298942--------
------------------------------------
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
----------
----------
----------
select sum(c.cantidad*c.preciounidad) venta_total
from 
clientes a inner  join pedidos b on a.idCliente=b.idCliente
            inner join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
		    inner join [dbo].[productos] d on c.idproducto=d.idproducto

------------------------------------
------- venta total: 1356335--------
------------------------------------
select a.idCliente from clientes a left  join clientes_88 b on a.idCliente=b.idCliente where b.idCliente is null
---
--- los 3 clientes quitados son :
---
----------------
--- idCliente---
----------------
-- PARIS
-- FISSA
-- HUNGO
------------------------------------
---
---
--- Crear una tabla con estos 3 "idCliente"
select *
into clientes_3
from
(
select a.idCliente from clientes a left  join clientes_88 b on a.idCliente=b.idCliente where b.idCliente is null
) as t1

--- hay 19 pedidos que hacen estas 3 personas 
select count(*) from Pedidos a  inner join clientes_3 b on a.IdCliente=b.idCliente
---
select   a.IdPedido from Pedidos a  inner join clientes_3 b on a.IdCliente=b.idCliente --- 19 filas o 19 IdCliente
---
select *
into pedidos_19
from 
(select   a.IdPedido from Pedidos a  inner join clientes_3 b on a.IdCliente=b.idCliente) as t1
---
select sum(b.cantidad*b.preciounidad) from
pedidos_19 a inner join detallesdepedidos b on a.IdPedido=b.idpedido
--- venta total por estos 3 clientes es 57393
---
---
select sum(a.cantidad*a.preciounidad) from detallesdepedidos a inner join pedidos b on a.idpedido=b.IdPedido
---1356335
---
----
---
---
select * from clientes--91 clientes !!!
---
---
---------------------------------------------------------------------------------------------------------
----------->>>>>>> 91 clientes  <<<<<< 
select  distinct  a.idCliente,count(b.IdPedido) numero_pedidos,sum(c.cantidad*c.preciounidad) venta_total,
sum(c.cantidad*c.preciounidad)/count(b.IdPedido) promedio_ventas
from 
clientes a left  join pedidos b on a.idCliente=b.idCliente
            left join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
		    left  join [dbo].[productos] d on c.idproducto=d.idproducto
group by a.idCliente

---creando tabla con 91 clientes
select *
into clientes_91
from
(select  distinct  a.idCliente,count(b.IdPedido) numero_pedidos,sum(c.cantidad*c.preciounidad) venta_total,
sum(c.cantidad*c.preciounidad)/count(b.IdPedido) promedio_ventas
from 
clientes a left  join pedidos b on a.idCliente=b.idCliente
            left join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
		    left  join [dbo].[productos] d on c.idproducto=d.idproducto
group by a.idCliente)as t1
----
----
select *
from  clientes_91 where venta_total is null
/*cometario:
-----------
idCliente numero_pedidos venta_total  promedio_ventas 
 PARIS           0         NULL             NULL
 FISSA           0         NULL             NULL 
*/
/*>>>>>>>>>>>>>> clientes 91 <<<<<<<<<<<<<<<<*/
select *
into clientes_91
from 
(
select distinct a.idCliente,count(b.IdPedido) numero_pedidos,sum(c.cantidad*c.preciounidad) venta_total,
sum(c.cantidad*c.preciounidad)/count(b.IdPedido) promedio_ventas
from 
clientes a left  join pedidos b on a.idCliente=b.idCliente
            left join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
		    left join [dbo].[productos] d on c.idproducto=d.idproducto
group by  a.idCliente) as t1
----
----
----
select *
from clientes_91
-----
-----
-----

select * from clientes
----
select ,sum(cantidad*preciounidad) from detallesdepedidos

select a.idCliente,sum(c.cantidad*c.preciounidad)
from 
clientes a left  join pedidos b on a.idCliente=b.idCliente
            left join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
group by a.idCliente

select *
into venta_total
from
(select a.idCliente,sum(c.cantidad*c.preciounidad) venta_total
from 
clientes a left  join pedidos b on a.idCliente=b.idCliente
            left join [dbo].[detallesdepedidos] c on b.IdPedido=c.idpedido
group by a.idCliente) as t1


select *
from venta_total
---1356335

select *
from venta_total where idCliente like 'HUNGO' --venta total 57393
/*HUNGO*/

/*
idCliente numero_pedidos venta_total  promedio_ventas 
 PARIS           0         NULL             NULL
 FISSA           0         NULL             NULL 
*/
select * from venta_total where idCliente like 'HUNGO' --venta total 0

select * from categorias where nombrecategoria like 'bebidas'--1
select * from productos where idCategoria like '1'--12

/*******************************************************/
/* productos*/
select sum(a.cantidad*a.preciounidad) from 
detallesdepedidos a  inner join productos b on a.idproducto=b.idproducto
                     inner join categorias c on b.idCategoria=c.idcategoria
where c.nombrecategoria like 'bebidas'		
--- 286974
SELECT * FROM Empleados
          
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
select * from [dbo].[categorias]
select * from [dbo].[clientes]
select * from [dbo].[compañiasdeenvios]
select * from [dbo].[detallesdepedidos]
select * from [dbo].[Empleados]
select * from [dbo].[Pedidos]
select * from [dbo].[productos]
select * from [dbo].[proveedores]
--------------------------------
--------------------------------
select top 2 * from clientes_91