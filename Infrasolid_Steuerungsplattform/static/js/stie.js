function dataReader(){
    // Construct the URL with query parameters
const queryParams = new URLSearchParams({ ip: '10.10.0.5' });
const apiUrl = `/api/hmp4040_measure/?${queryParams.toString()}`;

// Send the GET request
fetch(apiUrl, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        // You can include other headers if needed, such as authentication tokens
    }
})
.then(response => response.json())
.then(data => {
    for( let i = 1; i<5;i++ ){
        const vp = document.getElementById('v_ch' + i);
        const Ip = document.getElementById('I_ch' + i);
        const Pp = document.getElementById('P_ch' + i);
        vp.textContent = data[i][0].toFixed(3) + "  V";
        Ip.textContent = data[i][1].toFixed(3)  + "  A";
        Pp.textContent = data[i][2].toFixed(3)  + "  W";
    }
})
.catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Error:', error);
});

}
dataReader()
const intervalId = setInterval(dataReader, 60000);