$('document').ready(()=>{
  $('#createform').submit((event)=>{
    event.preventDefault()
    pitch=$('#Pitch').val().trim()
    category=$('#catchoose').val().trim()
    if (pitch.length < 2){return}
    $.ajax(
      {
        url:'/newpitch',
        data:{
          'pitch':pitch,
          'category':category
        },
        method:'GET',
        success:(data)=>{
          $("#pitches").prepend(data)
          $('#createform')[0].reset()
        },
        error: (data)=>{
          alert('Could not post pitch')
        }
      }
    )
  });
  submitcomment=(postid)=>{
    $.post('/comments/'+postid, $('form#comment'+postid).serialize(),(data)=>{
      $(data).hide().appendTo($('#comments'+postid)).show('fast');
      count=$('#commentscount'+postid)
      count.text(parseInt(count.text())+1)
    });
  }

  $('.toggle').click(function(){
    // Switches the Icon
    $(this).children('i').toggleClass('fa-pencil');
    // Switches the forms  
    $('.form').animate({
      height: "toggle",
      'padding-top': 'toggle',
      'padding-bottom': 'toggle',
      opacity: "toggle"
    }, "slow");
  });

  $(function() {
    $('.search a').on('click', function() {
        $('.search input').fadeToggle('400').focus();
        $(this).toggleClass('active');
        return false;
    });
  });
});