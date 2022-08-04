import React from 'react'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import About from './components/About'
import NavBar from './components/NavBar'
import Users from './components/Users'

const App = () => {
  return (
    <BrowserRouter>
      <NavBar/>
      <Routes>
        <Route path='/about' element={<About/>} />
        <Route path='/' element={<Users/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App