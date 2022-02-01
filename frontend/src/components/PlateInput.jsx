import React, {useState} from 'react';
import './App.css'
import 'bootstrap/dist/css/bootstrap.css';

export function PlateInput() {
    
    const [plate, setPlate] = useState('');
    const [model, setModel] = useState('');
    
    // convertir a arrow/lambda functions?
    function updatePlate(val)
    {
        setPlate(val.target.value);
    }
    function sendPlate()
    {
        setModel(plate)
        console.log(plate);
        // Placeholder para ¿la función lambda?
    }
      
    return (
        <div class="xy-center col">
            <div class="text-center my-5">
                <h1 class="mb-5 display-1 b">Ver modelo de auto</h1>
                
                <div class="mx-auto h4" style={{width: '75%', height: '30%'}}>
                    <input type="text" onChange={updatePlate} style={{float: 'left', width: '80%', height: '100%'}}/>
                    <button onClick={sendPlate} style={{float: 'right', width: '20%', height: '100%'}}> Enviar </button>
                </div>
                {
                    model?
                    <h3>Modelo del auto: {model}</h3>
                    :null
                }
            </div>  
        </div>
    );
}
