// אלמנטים שמקבלים את הקלאס הזה לוחצים על כפתור הואלידאציה כאשר הם נלחצים
$(".myvalidate").change(function(){
  document.getElementById("Submit").click();
});

$(document).ready(function(){
  if(variables.reloder==1){
    document.getElementById("Submit").click();
  }
  var privileges = document.getElementsByClassName("UserPrivilege");
  for(p in privileges){
    if(conected){
      privileges[p].classList.remove("disabled")
    }else{
      privileges[p].classList.add("disabled")
    }};
});


if(document.getElementById("id_list").value !=""){
  $(".kupotChangeWatcher").click(function(){
    const myModal = new bootstrap.Modal('#changeWarningModal');
    myModal.toggle()
    $("#kupaChanger").click(function(){
      document.getElementById("id_list").value ="";
      document.getElementById("Submit").click();
    });
  $("#myCloseModal").click(function(){
    document.querySelector('input[name="kupa_type"][value="' + variables.Polytop_What + '"]').checked = true;
      subTypeDisplay(variables.Polytop_What);
  })
});
}else{
  $(".kupotChangeWatcher").click(function(){
      document.getElementById("Submit").click();
  })
};
//activates popovers
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
 // מדפיס את תוכן הדף ל-pdf
function myPrint(){
window.print();
  };

// toggle menahalim
$(".menahalim").change(function(){
  if ($(this).val() !== "בחרו מנהל") {
    $("#all_menahalim").prop("checked", false);
  }
});
$("#all_menahalim").change(function() {
  if($(this).prop("checked")) {
    $(".menahalim").each(function(){
      $(this).val("בחרו מנהל")
    });
  }
})

function kupotNivharot(reshima,thi){
  const kupaList=document.getElementById("id_list").value.split(",")//רשימת קופות שמורות
  let clickedKupa=$(thi).text().match(/\d+/)[0]//מספר הקופה שנלחצה

  function checkInId(i){
    return i == clickedKupa
  }//בודק אם מספר הקופה שנלחצה שווה לאלמנטים ברשימת הקופות

    //בודק אם אלמנטים מסויימים נבחרו כבר לצורך השוואה ולפי זה פועל
    if(kupaList.some(checkInId)) {//קורה אם האלמנט נמצא כבר ברשימה

        document.getElementById("id_list").value = document.getElementById("id_list").value.replace((clickedKupa+","),"");//מוחק ת"ז מהרשימה

        for(i in document.getElementsByClassName("selectedKupa")){
          if(document.getElementsByClassName("selectedKupa")[i].innerText == thi.getElementsByTagName("td")[0].textContent){
            document.getElementById("selected_group").deleteRow(i)}};//מוחק שורה של הקופה שנלחצה מהרשימה

          document.getElementById("Submit").click();//מעדכן את הדף

    }else{//קורה אם האלמנט לא נמצא ברשימה
      if(kupaList.length < 5){
      document.getElementById("selected_group").innerHTML = document.getElementById("selected_group").innerHTML
      +"<tr>"+"<td style='display:none;' class='selectedKupa'>"+thi.getElementsByTagName("td")[0].textContent+"</td>"+"<td style='width:100%;'>"+thi.getElementsByTagName("td")[4].textContent+"</td>"+"</tr>";//מוסיף את שם הקופה שנלחצה לרשימה של הקופות להשוואה

      document.getElementById("id_list").value = document.getElementById("id_list").value+(clickedKupa+",");//מוסיף את מספר הקופה  לרשימת הת"ז של הקופות

      document.getElementById("Submit").click();//מעדכן את הדף

      }else{
        const alertPlaceholder = document.getElementById('myAlertLim')

        const alert = (message, type) => {
          const wrapper = document.createElement('div')
          wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
          ].join('')

          alertPlaceholder.append(wrapper)
        }
            alert('בחירת הקופות להשוואה מוגבלת לארבע ', 'warning')//יוצר הודעה שקופצת כאשר מנסים לבחור יותר מ 4 קופות
      }}
  };

$(".kupaSel").click(function(){kupotNivharot("kupaSel",this)});
$(".kupaSelectedRow").click(function(){kupotNivharot("kupaSelectedRow",this)});

//הופך את כפתור השוואת הקופות ללא פעיל אם מספר הקופות הנבחרות קטן מ-2 ומחזיר אותו לפעולה אם יש 2 או יותר קופות נבחרות
$(document).ready(function(){
  const kupaList=document.getElementById("id_list").value.split(",")
  if(kupaList.length <= 2){
    document.getElementById("coopComp").classList.add("disabled")
  }else{
    document.getElementById("coopComp").classList.remove("disabled")
  }});

// תפקוד שמיצא מידע לאקסל
function exportData(){
    /* Get the HTML data using Element by Id */
    var table = document.getElementById("kupotTable");
    /* Declaring array variable */
    var rows =[];
      //iterate through rows of table
    for(var i=0,row; row = table.rows[i];i++){
        //rows would be accessed using the "row" variable assigned in the for loop
        //Get each cell value/column from the row
      if(rows.length<variables.excelLimitor){
          column1 = row.cells[1].innerText;
          column2 = row.cells[2].innerText;
          column3 = row.cells[3].innerText;
          column4 = row.cells[4].innerText;
          column5 = row.cells[5].innerText;
          column6 = row.cells[6].innerText;
          column7 = row.cells[7].innerText;
          column8 = row.cells[8].innerText;
          column9 = row.cells[9].innerText;
          column10 = row.cells[10].innerText;
      var BOM = "\uFEFF";
      /* add a new records in the array */
          rows.push(
              [column1,column2,column3,column4,column5,
              column6,column7,column8,column9,column10]);
        }}
        csvContent = "data:text/csv;charset=utf-8," + BOM;
         /* add the column delimiter as comma(,) and each row splitted by new line character (\n) */
        rows.forEach(function(rowArray){
            row = rowArray.join(",");
            csvContent += row + "\r\n";
        });
        /* create a hidden <a> DOM node and set its download attribute */
        var encodedUri = encodeURI(csvContent);
        var link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "קופות.csv");
        document.body.appendChild(link);
         /* download the data file named "קופות.csv" */
        link.click();
}


// קובע את תכונות הטווח הנבחר
$("#migbelet_menayot").ionRangeSlider({
type: "double",
skin: "round",
grid: true,
min: 0,
max: 100,
from: Math.floor(variables.min_menayot*100),
to: Math.floor(variables.max_menayot*100)
});

$("#migbelet_matach").ionRangeSlider({
type: "double",
skin: "round",
grid: true,
min: 0,
max: 100,
from: Math.floor(variables.min_matach*100),
to: Math.floor(variables.max_matach*100)
});
//טווח נבחר ספציפי לדרגות סיכון
// $(".myRangeSlider").ionRangeSlider({
// type: "single",
// grid: true,
// min: 0,
// max: 10,
// from: 0,
// to: 10
// });

// מעביר את הנתונים מהסלידר לאלמנט נסתר שפיתון יכול לקרוא
function setSliderValue(el){
  let hidden_min = el.attr("for_min");
  let hidden_max = el.attr("for_max");
  $(`[name='${hidden_min}']`).val(el.data("from"));
  $(`[name='${hidden_max}']`).val(el.data("to"));
}

// connect range sliders to hidden fields
$(".js-range-slider").each(function () {
  setSliderValue($(this))
});
$(".js-range-slider").change(function () {
  setSliderValue($(this))
});
//אותו התפקוד לטווח של דרגות הסיכון
// $(".myRangeSlider").each(function () {
//   setSliderValue($(this))
// });
// $(".myRangeSlider").change(function () {
//   setSliderValue($(this))
// });

// שם את  ברירת המחדל לבחירות התת קופה בהתחלת הדף
let sel = document.getElementsByClassName("input-group");

function subTypeDisplay(button){
  if(button==2){
    sel[0].style.display = "block";
    sel[1].style.display = "none";
    sel[2].style.display = "none";
  }else if(button==1){
    sel[0].style.display = "none";
    sel[1].style.display = "block";
    sel[2].style.display = "none";
  }else if(button==8){
    sel[0].style.display = "none";
    sel[1].style.display = "none";
    sel[2].style.display = "none";
  }else if(button== 3){
    sel[0].style.display = "none";
    sel[1].style.display = "none";
    sel[2].style.display = "block";
  }else{
    sel[0].style.display = "none";
    sel[1].style.display = "none";
    sel[2].style.display = "none";
  };
}
//שומר את הצגת תת הקופה הנכונה בין טעינות של הדף
$(document).ready(function(){
  subTypeDisplay(variables.Polytop_What);
  switch (variables.Polytop_What) {
    case 2:
      document.getElementById("kupa_type-3").previousElementSibling.classList.add("btn-dark");
      document.getElementById("kupa_type-3").previousElementSibling.classList.remove("btn-outline-dark");
      break;
    case 1:
      document.getElementById("kupa_type-0").previousElementSibling.classList.add("btn-dark");
      document.getElementById("kupa_type-0").previousElementSibling.classList.remove("btn-outline-dark");
      break;
    case 8:
      document.getElementById("kupa_type-2").previousElementSibling.classList.add("btn-dark");
      document.getElementById("kupa_type-2").previousElementSibling.classList.remove("btn-outline-dark");
      break;
    case 3:
      document.getElementById("kupa_type-1").previousElementSibling.classList.add("btn-dark");
      document.getElementById("kupa_type-1").previousElementSibling.classList.remove("btn-outline-dark");
      break;
    default:

  }
});

// משנה את בחירות התת קופה לפי כפתור סוג הקופה שנבחר
let elements = document.getElementsByClassName("checker")
Array.from(elements).forEach(function(element) {

  element.addEventListener("click", function(){
    subTypeDisplay(this.value);
  let all_nav_items = this.closest(".nav").querySelectorAll("label");
  for (let nav_item of all_nav_items) {
    nav_item.classList.remove("btn-dark")
    nav_item.classList.add("btn-outline-dark")

  };
    this.previousElementSibling.classList.remove("btn-outline-dark");
    this.previousElementSibling.classList.add("btn-dark");

  });
});
//מוסיף את ההודעות הקופצות שנשלחות לדף בהירשמות,התחברות והתנתקות
$(document).ready(function(){
  for(i in myAlerts){
  const alertPlaceholder = document.getElementById('myAlertLim')

  const alert = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
      `<div class="alert alert-${type} alert-dismissible" role="alert">`,
      `   <div>${message}</div>`,
      '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
      '</div>'
    ].join('')

    alertPlaceholder.append(wrapper)
  }
      alert(myAlerts[i], 'success')
  }})

// שומר את הבחירות של הקופות וגם צובע את הקופות השמורות אחרי לחיצה על החיפוש !קוד שבא אחרי זה לא מתפקד ולכן חייב להיות בתחתית! חשוב
function kupotNivharotLoad(reshima){

for(i in document.getElementsByClassName(reshima)) {// על כל שורה בשורות הקופה
    let kupaNum=document.getElementsByClassName(reshima)[i].children[0].innerHTML
    const kupaList=document.getElementById("id_list").value.split(",")

    function myLogicTest(test){
     return test ==kupaNum
    }
  if(kupaList.some(myLogicTest)) {//אם מספר קופה בתוך התפקוד
    document.getElementsByClassName(reshima)[i].classList.add("table-success");//משנה את הצבע של הקופה לירוק
    document.getElementById("selected_group").innerHTML = document.getElementById("selected_group").innerHTML
    +"<tr>"+"<td style='display:none;' class='selectedKupa'>"+document.getElementsByClassName(reshima)[i].children[0].innerHTML+"</td>"+"<td style='width:800px;'>"+document.getElementsByClassName(reshima)[i].children[4].innerHTML+"</td>"+"</tr>";//מוסיף את שם הקופה בחזרה לרשימה של הקופות שנבחרו
  }}};

$(document).ready(function(){
  kupotNivharotLoad("kupaSelectedRow")
  });

  $(document).ready(function(){
    for(kupaNameIndex in document.getElementsByClassName("kupaSel")){
      for (kupaId of document.getElementById("id_list").value.split(",")){
          if (document.getElementsByClassName("kupaSel")[kupaNameIndex].getElementsByClassName("IdKupa")[0].innerText == kupaId){
            let myIndex= Number(kupaNameIndex) + document.getElementsByClassName("kupaSelectedRow").length
            document.getElementById("mainTable").deleteRow(myIndex)}}}
  });
