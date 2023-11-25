import SearchBar from '@/components/searchBar'
import Head from 'next/head'
import { Box, Center } from '@chakra-ui/react'
import { useState } from 'react'
import Filters from '@/containers/filters'
import axios from 'axios'
export default function Home() {
  const [searchTerm, setSearchTerm] = useState('')
  const handleSearch = (event) => {
    event.preventDefault()
    axios.get(`http://localhost:8000/api/search?search=${searchTerm}`)
      .then(res => {
        console.log(res.data)
      })
  }
  return (
    <>
      <Head>
        <title>App</title>
        <meta name="description" content="Sample django next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="">
        <Center>
          <Box mt={20} mx={'auto'}  >
            <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} handleSearch={handleSearch} />
            <Filters />
          </Box>
        </Center>

        {/* <Filters /> */}
      </main>
    </>
  )
}
