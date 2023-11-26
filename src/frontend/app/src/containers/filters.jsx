import React, { useEffect } from 'react'
import RangeFilter from '@/components/rangeFilter';
import { Box, Flex, Text, NumberInput, NumberInputField, NumberInputStepper, NumberIncrementStepper, NumberDecrementStepper } from '@chakra-ui/react';
import { useState } from 'react';
import SiteFilter from '@/components/siteSelect';
const Filters = ({
    review,
    rating,
    price,
    totalResults,
    webSites,
    setReview,
    setRating,
    setPrice,
    setTotalResults,
    setWebSites
}) => {


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
                < RangeFilter label="Price" min={price.min} max={price.max}
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
