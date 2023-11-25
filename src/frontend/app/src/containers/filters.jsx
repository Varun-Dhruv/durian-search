import React, { useEffect } from 'react'
import RangeFilter from '@/components/rangeFilter';
import { Box, Flex, Text, NumberInput, NumberInputField, NumberInputStepper, NumberIncrementStepper, NumberDecrementStepper } from '@chakra-ui/react';
import { useState } from 'react';
import SiteFilter from '@/components/siteSelect';
const Filters = () => {
    const [review, setReview] = useState({
        min: 0,
        max: 5
    })
    const [rating, setRating] = useState({
        min: 0,
        max: 100000
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
        ebay: true,
        paytm: true,
    })

    return (
        <Box mt={10}>

            <Flex direction="column" gap={5} align={"center"} mx="auto">
                <RangeFilter label="Review" min={review.min} max={review.max}
                    handleMin={(val) => {
                        setReview((prev) => { return { ...prev, min: val } })
                    }}
                    handleMax={(val) => {
                        setReview((prev) => { return { ...prev, max: val } })
                    }} />
                <RangeFilter label="Rating" min={rating.min} max={rating.max}
                    handleMin={(val) => {
                        setRating((prev) => { return { ...prev, min: val } })
                    }}
                    handleMax={(val) => {
                        setRating((prev) => { return { ...prev, max: val } })
                    }} />
                < RangeFilter label="Review" min={price.min} max={price.max}
                    handleMin={(val) => {
                        setPrice((prev) => { return { ...prev, min: val } })
                    }}
                    handleMax={(val) => {
                        setPrice((prev) => { return { ...prev, max: val } })
                    }} />

                <SiteFilter sites={webSites} setSites={setWebSites} />
                <Flex textAlign={'center'} my="auto" direction={'row'} gap={2}>
                    <Text mt={2}>Total Results :</Text>
                    <NumberInput
                        onChange={(val) => setTotalResults(val)}
                        value={totalResults}
                        max={10}
                    >
                        <NumberInputField />
                        <NumberInputStepper>
                            <NumberIncrementStepper />
                            <NumberDecrementStepper />
                        </NumberInputStepper>
                    </NumberInput>
                </Flex>

            </Flex >
        </Box >

    )
}
export default Filters;
