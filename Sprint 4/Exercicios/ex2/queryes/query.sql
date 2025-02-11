select nome, count(*) as qtd_n 
from meubanco.nomes
where ano >= 1950
group by nome
order by qtd_n desc
limit 3