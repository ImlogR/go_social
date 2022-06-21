
var formData = new FormData();

$(document).on('submit', '#write-post', function(e){
    e.preventDefault();

    formData.append("caption", $('#caption').val());
    formData.append("image", $('#image')[0].files[0]);
    formData.append("action", 'upload-ajax')
    formData.append("csrfmiddlewaretoken", "{{ csrf_token }}");
    $.ajax({
        type: "POST",
        url: "/upload",    
        data: formData, 
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function(){
            alert('The post has been created!')
        },
        error: function(xhr, errmsg, err){
            console.log(xhr.status + ":" + xhr.responseText)
        }
    });
});