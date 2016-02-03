$(document).ready(function() {
    $('[data-role=like_container]').on('click', '[data-action=like_button]', function(e){
        var $like_container = $(e.delegateTarget);
        var $like_button = $(e.currentTarget);
        var $vote_value = $like_container.find('[data-role=vote_value]');
        var link_id = $like_button.data("linkset_id");

        var nombre_tapa;

        nombre_tapa = $(this).attr("data-nombre-tapa");
        nombre_bar = $(this).attr("data-bar");


        $.get('/rango/voto_tapa/', {tapa_id: nombre_tapa, bar_slug: nombre_bar},  function(uplink_response){
               $('#voto_count').html(data);
            $vote_value.html(uplink_response);
            $like_button.hide();
    });
    });
});
