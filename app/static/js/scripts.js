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
    [...$(".commentinput")].forEach(c=>c.value='')
  }
});