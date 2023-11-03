const takePhoto = document.getElementById('take-photo');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');






function dataURItoBlob(dataURI) {
            const byteString = atob(dataURI.split(',')[1]);
            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            return new Blob([ab], { type: 'image/png' });
        }

        function getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        }

   function capturePhoto() {
            canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);

            console.log("Clicked........");
            const dataUrl = canvas.toDataURL();
            const blobData = dataURItoBlob(dataUrl);

            const formData = new FormData();
            formData.append('image', blobData, 'photo.png');

            fetch('get_frame', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => console.log("Response..", response))
            .then(() => {



            })
            .catch(error => {
   error.style.display ='block'
            });




        }


takePhoto.addEventListener('click', capturePhoto);
