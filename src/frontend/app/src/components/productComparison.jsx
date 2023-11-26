import React from 'react'
import { Box, Table, Thead, Tbody, Tfoot, Tr, Th, Td, TableCaption, TableContainer } from "@chakra-ui/react"

const ProductComparison = ({ productData }) => {
    return (
        <Box mx={24} my={24}>
            <TableContainer>
                <Table size='md'>
                    <Thead>
                        <Tr>
                            <Th>No.</Th>
                            <Th>Title</Th>
                            <Th>URL</Th>
                            <Th isNumeric>Total Review Count</Th>
                            <Th isNumeric>Rating</Th>
                            <Th isNumeric>Price</Th>
                            <Th>website</Th>
                        </Tr>
                    </Thead>
                    <Tbody>
                        {
                            productData?.map((product, key) => {
                                return (
                                    <Tr>
                                        <Td>{key + 1}</Td>
                                        <Td>{product.title.slice(0, 20) + "..."}</Td>
                                        <Td><a href={product.url}>{product.url.slice(0, 20) + "..."}</a></Td>
                                        <Td isNumeric>{product.total_review_count}</Td>
                                        <Td isNumeric>{product.rating}</Td>
                                        <Td isNumeric>{product.price}</Td>
                                        <Td>{product.website}</Td>
                                    </Tr>
                                )
                            })
                        }
                    </Tbody>
                    <Tfoot>
                        <Tr>
                            <Th>Title</Th>
                            <Th>URL</Th>
                            <Th isNumeric>Total Review Count</Th>
                            <Th isNumeric>Rating</Th>
                            <Th isNumeric>Price</Th>
                            <Th>website</Th>
                        </Tr>
                    </Tfoot>
                </Table>
            </TableContainer>
        </Box>
    )
}
export default ProductComparison
