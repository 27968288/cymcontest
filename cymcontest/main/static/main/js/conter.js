$(document).ready(function(){  
    
    $(document).on('click', 'a[id^=a]', function(){
      var idname = $(this).attr('id').slice(1,2);
      var html = idname + '.html';
      $('#conter').load(html);
       });
    $(document).on('click', 'button[id=closel]', function(){
      $('#Lside').text('為什麼不看一下OwQ');
    })
    $(document).on('click', 'button[id=closer]', function(){
      $('#Rside').text('真的不想看嗎OAQ');
    })
  });