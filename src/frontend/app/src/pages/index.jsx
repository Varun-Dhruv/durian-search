import SearchBar from '@/components/searchBar'
import Head from 'next/head'
import { Box, Center } from '@chakra-ui/react'
import { useState } from 'react'
import Filters from '@/containers/filters'
import axios from 'axios'
import ProductComparison from '@/components/productComparison'
export default function Home() {
  const [searchTerm, setSearchTerm] = useState('')

  const handleSearch = (event) => {
    event.preventDefault()
    let params = {
      minReview: review.min,
      maxReview: review.max,
      minRating: rating.min,
      maxRating: rating.max,
      minPrice: price.min,
      maxPrice: price.max,
      searchTerm: searchTerm,
      totalProducts: totalResults,
      websites: Object.keys(webSites).filter((key) => webSites[key]).join(','),
    }
    console.log(params)
    axios.get(`${process.env.NEXT_PUBLIC_SERVER_URL}/products`, { params: params })
      .then(res => {
        setProductData(res.data.products)
      }).catch(err => {
        console.log(err.response)
      })
  }
  const [productData, setProductData] = useState([])
  const [review, setReview] = useState({
    min: 0,
    max: 100000
  })
  const [rating, setRating] = useState({
    min: 0,
    max: 5
  })
  const [price, setPrice] = useState({
    min: 0,
    max: 100000
  })
  const [totalResults, setTotalResults] = useState(3)
  const [webSites, setWebSites] = useState({
    amazon: true,
    flipkart: true,
    snapdeal: true,
    blinkit: true,
    jiomart: true,
  })

  return (
    <>
      <Head>
        <title>Durian Search</title>
        <meta name="description" content="Durian Search a comparison tool" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="">
        <Center>
          <Box mt={20} mx={'auto'}  >
            <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} handleSearch={handleSearch} />
            <Filters
              review={review}
              rating={rating}
              price={price}
              totalResults={totalResults}
              webSites={webSites}
              setReview={setReview}
              setRating={setRating}
              setPrice={setPrice}
              setTotalResults={setTotalResults}
              setWebSites={setWebSites}
            />
          </Box>
        </Center>
        <ProductComparison productData={productData} />
        {/* <Filters /> */}
      </main>
    </>
  )
}
