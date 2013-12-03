$(function(){
    $('a[href^=#]').click(function(e){
        var name = $(this).attr('href').substr(1);
        var pos = $('article[id='+name+']').offset();
        var scroll = pos.top - 45
        $('body').animate({ scrollTop: scroll }, 1000);
        $('nav.top-bar').removeClass('expanded')
        $('nav.top-bar').parent().addClass('fixed')
        e.preventDefault();
    });
});
