
$( document ).ready(function() {
    $('.comment-form').hide()

    $('.comment-button').click(function(){
        $(this.parentNode.parentNode.getElementsByClassName('comment-form')[0]).slideToggle()
    }
    );
});