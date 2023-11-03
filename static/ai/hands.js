import DeviceDetector from "https://cdn.skypack.dev/device-detector-js@2.2.10";
import { measurements } from './calculations.js';
const mpHands = window;
const drawingUtils = window;
const controls = window;
const controls3d = window;
// Usage: testSupport({client?: string, os?: string}[])
// Client and os are regular expressions.
// See: https://cdn.jsdelivr.net/npm/device-detector-js@2.2.10/README.md for
// legal values for client and os
testSupport([
    { client: 'Chrome' },
]);
// Rest of your code remains unchanged
// ...

function testSupport(supportedDevices) {
    const deviceDetector = new DeviceDetector();
    const detectedDevice = deviceDetector.parse(navigator.userAgent);
    let isSupported = false;
    for (const device of supportedDevices) {
        if (device.client !== undefined) {
            const re = new RegExp(`^${device.client}$`);
            if (!re.test(detectedDevice.client.name)) {
                continue;
            }
        }
        if (device.os !== undefined) {
            const re = new RegExp(`^${device.os}$`);
            if (!re.test(detectedDevice.os.name)) {
                continue;
            }
        }
        isSupported = true;
        break;
    }
    if (!isSupported) {
        alert(`This demo, running on ${detectedDevice.client.name}/${detectedDevice.os.name}, ` +
            `is not well supported at this time, continue at your own risk.`);
    }
}


// Our input frames will come from here.
const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const controlsElement = document.getElementsByClassName('control-panel')[0];
const takePhoto = document.getElementById('take-photo');
const lengthSlider = document.getElementById('length');
const triggerSlider = document.getElementById('trigger');
const gripSlider = document.getElementById('grip');

lengthSlider.addEventListener('input', function () {
  const handSizeValueElement = document.getElementById('lValue');
  handSizeValueElement.textContent = lengthSlider.value;
});


triggerSlider.addEventListener('input', function () {
  const handSizeValueElement = document.getElementById('tValue');
  handSizeValueElement.textContent = triggerSlider.value;
});
gripSlider.addEventListener('input', function () {
  const handSizeValueElement = document.getElementById('gValue');
  handSizeValueElement.textContent = gripSlider.value;
});

 let landmark = [];

const canvasCtx = canvasElement.getContext('2d');
const config = { locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/hands@${mpHands.VERSION}/${file}`;
    } };
// We'll add this to our control panel later, but we'll save it here so we can
// call tick() each time the graph runs.
// const fpsControl = new controls.FPS();
// Optimization: Turn off animated spinner after its hiding animation is done.
const spinner = document.querySelector('.loading');
spinner.ontransitionend = () => {
    spinner.style.display = 'none';
};
const landmarkContainer = document.getElementsByClassName('landmark-grid-container')[0];
const grid = new controls3d.LandmarkGrid(landmarkContainer, {
    connectionColor: 0xCCCCCC,
    definedColors: [{ name: 'Left', value: 0xffa500 }, { name: 'Right', value: 0x00ffff }],
    range: 0.2,
    fitToGrid: false,
    labelSuffix: 'm',
    landmarkSize: 2,
    numCellsPerAxis: 4,
    showHidden: false,
    centered: false,
});
function onResults(results) {
  // Hide the spinner.
  document.body.classList.add('loaded');
  // Update the frame rate.
  // fpsControl.tick();
  // Draw the overlays.
  canvasCtx.save();
  canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
  canvasCtx.drawImage(results.image, 0, 0, canvasElement.width, canvasElement.height);
  if (results.multiHandLandmarks && results.multiHandedness) {
    for (let index = 0; index < results.multiHandLandmarks.length; index++) {
      const classification = results.multiHandedness[index];
      const isRightHand = classification.label === 'Right';
      const landmarks = results.multiHandLandmarks[index];

      if (landmark.length >= 14) {
        const handSize = measurements(landmarks);
        console.log("Distance between point 9 and 13:", handSize.hLength);
       // fpsControl.set('value', handSize);
      // Update the hand size value in the HTML

        if (handSize){

            //////Length/////////////////////////////
            const lValue = document.getElementById('lValue');
        lValue.textContent = handSize.hLength.toFixed(2);
        const length = document.getElementById('length');
        length.value = handSize.hLength;


        //////////////trigger////////////////////////

                 const tValue = document.getElementById('tValue');
        tValue.textContent = handSize.hTrigerLength.toFixed(2);
        const trigger = document.getElementById('trigger');
        trigger.value = handSize.hTrigerLength;


        ////////////////////grip///////////////////////////

                 const gValue = document.getElementById('gValue');
        gValue.textContent = handSize.hGripLength.toFixed(2);
        const grip = document.getElementById('grip');
        grip.value = handSize.hGripLength;

        }




      } else {
        console.log("Not enough landmarks to calculate distance.");
      }

      // Show point numbers and hand label
      for (let i = 0; i < landmarks.length; i++) {
        const point = landmarks[i];
        const [x, y] = [point.x * canvasElement.width, point.y * canvasElement.height];
        canvasCtx.fillText(`${i}`, x+1, y+1);
      }

      drawingUtils.drawConnectors(canvasCtx, landmarks, mpHands.HAND_CONNECTIONS, { color: isRightHand ? '#00FF00' : '#FF0000' });
      drawingUtils.drawLandmarks(canvasCtx, landmarks, {
        color: isRightHand ? '#00FF00' : '#FF0000',
        fillColor: isRightHand ? '#FF0000' : '#00FF00',
        radius: (data) => {
          return drawingUtils.lerp(data.from.z, -0.15, 0.1, 10, 1);
        }
      });
    }
  }
  canvasCtx.restore();

  if (results.multiHandWorldLandmarks) {
    // We only get to call updateLandmarks once, so we need to cook the data to
    // fit. The landmarks just merge, but the connections need to be offset.
    const landmarks = results.multiHandWorldLandmarks.reduce((prev, current) => [...prev, ...current], []);
    let connections = [];
    const colors = [];
    landmark = landmarks;

    for (let loop = 0; loop < results.multiHandWorldLandmarks.length; ++loop) {
      const offset = loop * mpHands.HAND_CONNECTIONS.length;
      const offsetConnections = mpHands.HAND_CONNECTIONS.map((connection) => [connection[0] + offset, connection[1] + offset]);
      connections = connections.concat(offsetConnections);

      const classification = results.multiHandedness[loop];

      colors.push({
        list: offsetConnections.map((unused, i) => i + offset),
        color: classification.label,
      });
    }
    grid.updateLandmarks(landmarks, connections, colors);
  } else {
    grid.updateLandmarks([]);
  }
}

const hands = new mpHands.Hands(config);
hands.onResults(onResults);
// Present a control panel through which the user can manipulate the solution
// options.
function toggleControlPanelVisibility() {
  controlsElement.classList.toggle('hidden');
}
new controls
    .ControlPanel(controlsElement, {

        selfieMode: true,
    maxNumHands: 2,
    modelComplexity: 1,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5,

})
    .add([
    new controls.StaticText({ title: 'First Line Of Defence' }),
    // fpsControl,

    new controls.SourcePicker({

        onFrame: async (input, size) => {
            const aspect = size.height / size.width;
            let width, height;
            if (window.innerWidth > window.innerHeight) {
                height = window.innerHeight;
                width = height / aspect;
            }
            else {
                width = window.innerWidth;
                height = width * aspect;
            }
            canvasElement.width = width;
            canvasElement.height = height;
            await hands.send({ image: input });
        },
    }),
    new controls.Slider({
        title: 'Max Number of Hands',
        field: 'maxNumHands',
        range: [1, 4],
        step: 1
    }),

    new controls.Slider({
        title: 'Model Complexity',
        field: 'modelComplexity',
        discrete: ['Lite', 'Full'],
    }),
    new controls.Slider({
        title: 'Min Detection Confidence',
        field: 'minDetectionConfidence',
        range: [0, 1],
        step: 0.01
    }),
    new controls.Slider({
        title: 'Min Tracking Confidence',
        field: 'minTrackingConfidence',
        range: [0, 1],
        step: 0.01
    }),
])
    .on(x => {
    const options = x;
    videoElement.classList.toggle('selfie',toggleControlPanelVisibility());
    hands.setOptions(options);



});



     function dataURItoBlob(dataURI) {
            const byteString = atob(dataURI.split(',')[1]);
            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            return new Blob([ab], { type: 'image/png' });
        }
function stopVideo() {
    if (videoElement.srcObject) {
        const stream = videoElement.srcObject;
        const tracks = stream.getTracks();

        tracks.forEach(function(track) {
            track.stop();
        });

        videoElement.srcObject = null;
    }
}

function captureAndSavePhoto() {
    // Capture the photo.
    // canvasCtx.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
     canvasElement.getContext('2d').drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
    // Get the image data from the canvas.
       const dataUrl = canvasElement.toDataURL();


    // Convert data URI to Blob.
    const blobData = dataURItoBlob(dataUrl);

    // Create a FormData object to send the image.
    const formData = new FormData();
    formData.append('image', blobData, 'photo.png');

    // Send the image data to the server using fetch.
    fetch('get_frame', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
        .then(response => {
            if (response.ok) {
                console.log("Image successfully saved.");
            } else {
                console.error("Failed to save the image.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });

    // Create a link element to download the image (optional).
    // const downloadLink = document.createElement("a");
    // downloadLink.href = imageData;
    // downloadLink.download = "photo.png";
    // downloadLink.click();
}

function takePhotoAndStopVideo() {
    console.log("Clicked...");
    // Stop the video.
    // stopVideo();
    console.log(landmark)
    // Capture and save the photo.
    captureAndSavePhoto();
}

// takePhoto.addEventListener('click', takePhotoAndStopVideo);