import React, {useState} from 'react';
import './App.css'
import 'bootstrap/dist/css/bootstrap.css';

export function PlateInput() {
    
    const [plate, setPlate] = useState('');
    const [model, setModel] = useState('');
    

    function updatePlate(val)
    {
        setPlate(val.target.value);
    }
    function sendPlate()
    {
        const url = "http://<host ip>:8000/getCarName/byPlate/" + plate.toUpperCase();

        var http = new XMLHttpRequest();
        http.open("GET", url, false);
        http.send(null);
        var jsonObject = JSON.parse(http.responseText);

        if (jsonObject != null)

        {
            setModel('Car model: ' + jsonObject['carManufacturer'] + ', ' +jsonObject['carModel']);
        }
        else
        {
            setModel('Car plate not found');
        }
    }

    return (
        <div>
            <div class="xy-center" style={{marginTop: '10px'}}>
                <div class="text-center my-5">
                    <h1 class="mb-5 display-1" style={{fontWeight: 'bold'}}>Car Model Finder</h1>
                    
                    <div class="mx-auto h4" style={{width: '75%', height: '30%'}}>
                        <input type="text" onChange={updatePlate} style={{float: 'left', width: '75%', height: '100%'}}/>
                        <button onClick={sendPlate} style={{float: 'right', width: '25%', height: '100%'}}>Send</button>
                    </div>
                </div>  
            </div>

            <div class="text-center">
                {
                    model?
                    <h3>{model}</h3>
                    :null
                }
            </div>
        </div>
    );
}
