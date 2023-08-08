$("#search_deals").autocomplete({
  source: function(request, response) {
    var search = $('#search_deals').val();
    $.ajax({
      type: 'get',
      url: '/flip/search/'+search,
      success: function(data){
           response($.map(data, function(c) {
             return {
                 label: c.title,
                 value: c.id
             }
           }).slice(0,10));

     }
   });
 },
 select: function( event, ui ) {
            window.location = "/flip/view/"+ui.item.value;
  }
});