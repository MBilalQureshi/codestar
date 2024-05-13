// In the context of JavaScript usage with Django, why is it important to construct URLs for edit and delete operations?
// To dynamically generate correct URLs.
// correct
// Answer
// Correct:Well done! JavaScript can dynamically generate URLs corresponding to specific items to edit or delete, interacting with Django's URL dispatcher.


// edit comment variables
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

// Delete comment variables
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    // For the delete functionality, the JavaScript determines which comment we aim to delete based on its ID.

    // deleteConfirm.href = `delete_comment/${commentId}`;
    // This code ensures that the delete link on the modal's confirmation button is updated with the right comment ID. Therefore, when the user confirms the deletion,
    // Django receives the correct URL and knows which comment to remove from the database.
    // "CALLS THE VIEWS IN BAKGROUND FROM HERE"
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";

  // The JavaScript code also modifies the comment form's action attribute to ensure it knows which comment it is updating when you click the Edit button:

  // commentForm.setAttribute("action", `edit_comment/${commentId}`);
  // Here, the code constructs the appropriate action URL for the comment being edited. When the form is submitted, this updated URL directs Django to the comment in the database that needs updating.

  // Note: An action value on a form appends onto the current URL. As the user is viewing the specific blog post, this post's <slug:slug>/ is already part of the URL and only edit_comment/<int:comment_id> is needed to complete the URL path with the action attribute. For example:

  // form action = "edit_comment/7"> // returns http://urladdress.com/<slug:slug>/edit_comment/7
  // "CALLS THE VIEWS IN BAKGROUND FROM HERE"
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}