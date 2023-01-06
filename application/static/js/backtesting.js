/*$(".backtestingInput").change(function(){
    let rows=document.getElementsByClassName("backtestingInput")
    const myArrey = ["length","item"]
    for(i in rows){
      if(myArrey.includes(i)){break}
        var sugKupa=rows[i].getElementsByClassName("myKupaType")[0].value;
        var menahelKupa=rows[i].getElementsByClassName("myMenahelKupa")[0].value;
        var options=backtestSearcher(sugKupa,menahelKupa);
        document.getElementById("test"+i).innerHTML=options;
        document.getElementById("mykupaName"+i).innerHTML="<option value='options'>"+options+"</option>";
    };
    })*/