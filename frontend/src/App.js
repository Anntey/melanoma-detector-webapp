import React, { useState } from 'react'
import './App.css'
import { Input, Header, Image, Segment } from 'semantic-ui-react'
import axios from 'axios'

const App = () => {
  const [fileUrl, setFileUrl] = useState('')
  const [pred, setPred] = useState(null)

  // ping backend
  axios.get('http://localhost:8000/ping').then(res => console.log(res.data))

  const handleFileChange = (event) => {
    event.preventDefault()

    const inputFile = event.target.files[0]

    if (inputFile) {
      setFileUrl(URL.createObjectURL(inputFile))

      const formData = new FormData()
      formData.append('img', inputFile, inputFile.name)

      const config = {
        headers: [
          { 'Content-Type': 'multipart/form-data' },
          { 'Access-Control-Allow-Origin': '*' }
        ]
      }

      axios
        .post('http://localhost:8000/predict', formData, config)
        .then(response => {
          const prob = parseFloat(response.data.prediction)
          setPred(prob)
        })
    }
  }

  return (
    <div className='App'>
      <Segment className='Segment'>

        <Header className='Header'>Please upload an image</Header>

        <div className='Img'>
        {fileUrl
          ? <Image src={fileUrl} />
          : <Image src={'https://react.semantic-ui.com/images/wireframe/image.png'} />
        }
        </div>

        <Input
          className='Input'
          type='file'
          onChange={handleFileChange}
        />
        

        <div className='Prediction'>
        {pred
          ? <h2>Prediction: {(pred * 100).toFixed(3)} %</h2>
          : ''
        }
        </div>
        

      </Segment>
      <div className='Footer'>Made by <a href={'https://github.com/anntey'}>Anntey</a></div>
    </div>
  )
}

export default App
