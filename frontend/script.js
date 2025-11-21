document.getElementById("predictForm").addEventListener("submit",async e=>{
e.preventDefault();const data={};new FormData(e.target).forEach((v,k)=>data[k]=v);
const res=await fetch("http://127.0.0.1:5000/predict",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(data)});
document.getElementById("result").innerText=JSON.stringify(await res.json(),null,2);});