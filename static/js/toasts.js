function showToast(message, messageType) {
    // Create a new toast element
    const toastElement = document.createElement('div');
    toastElement.classList.add('toast', 'align-items-center');

    // Set the appropriate Bootstrap alert class based on messageType
    switch (messageType) {
        case 'success':
            toastElement.classList.add('bg-success', 'text-light');
            break;
        case 'info':
            toastElement.classList.add('bg-info', 'text-light');
            break;
        case 'warning':
            toastElement.classList.add('bg-warning', 'text-dark');
            break;
        case 'error':
            toastElement.classList.add('bg-danger', 'text-light');
            break;
        default:
            // Default to success if messageType is not provided or invalid
            toastElement.classList.add('bg-success', 'text-light');
            break;
    }

    // Set the position and padding
    toastElement.classList.add('position-fixed', 'bottom-0', 'end-0');

    // Create the inner structure for the toast
    toastElement.innerHTML = `
      <div class="d-flex">
        <div class="toast-body">
          ${message}
        </div>
        <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
    `;

    // Append the toast element to the document
    document.body.appendChild(toastElement);

    // Initialize the Bootstrap toast component
    const toast = new bootstrap.Toast(toastElement);

    // Show the toast
    toast.show();
}