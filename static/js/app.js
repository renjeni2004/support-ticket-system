
const API='/api/'

function show(id){
document.getElementById('dashboard').style.display='none'
document.getElementById('new').style.display='none'
document.getElementById('all').style.display='none'
document.getElementById(id).style.display='block'

if(id=='dashboard')loadStats()
if(id=='all')loadTickets()
}

async function loadStats(){
let r=await fetch(API+'stats/')
let d=await r.json()
t_total.innerText=d.total
t_open.innerText=d.open
t_critical.innerText=d.critical
}

async function submitTicket(){

let data={
title:title.value,
description:desc.value,
category:cat.value,
priority:pri.value
}

await fetch(API+'tickets/',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify(data)
})

alert('Ticket submitted')
show('dashboard')
}

async function loadTickets(){

let r=await fetch(API+'tickets/')
let d=await r.json()

list.innerHTML=''

d.forEach(t=>{
let el=document.createElement('div')
el.className='card p-2 mb-2'
el.innerHTML=`
<b>${t.title}</b><br>
${t.category} | ${t.priority} | ${t.status}
`
list.appendChild(el)
})
}

loadStats()
