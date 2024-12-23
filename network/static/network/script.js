function editPost(element) {
    var postId = element.getAttribute('data-edit-post-id');
    document.getElementById('post-text-' + postId).style.display = 'none';
    document.getElementById('edit-options-' + postId).style.display = 'block';
}


function savePost(postId) {
    var updatedContent = document.getElementById('edit-textarea-' + postId).value;
    fetch(`/post/update/${postId}/`, {
        method: 'POST',
        body: new URLSearchParams({
            'post': updatedContent
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Post updated successfully.") {
            document.getElementById('post-text-' + postId).innerText = updatedContent;
            document.getElementById('post-text-' + postId).style.display = 'block';
            document.getElementById('edit-options-' + postId).style.display = 'none';
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        alert("An error occurred while updating the post.");
    });
}


function cancelEdit(postId) {
    document.getElementById('edit-options-' + postId).style.display = 'none';
    document.getElementById('post-text-' + postId).style.display = 'block';
}


function toggleLike(postId) {
    fetch(`/like/${postId}/`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        const likeCount = document.querySelector(`#like-count-${postId}`);
        likeCount.innerText = data.like_count;
    })
    .catch(error => console.error('Error:', error));
}
