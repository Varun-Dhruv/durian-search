import React from 'react'
import { Stack, Checkbox } from '@chakra-ui/react';
const SiteFilter = ({ sites, setSites }) => {
    return (
        <>
            <Stack spacing={[1, 5]} direction={['column', 'row']}>
                {
                    Object.keys(sites).map((site) => {
                        return (<Checkbox
                            size='lg'
                            colorScheme='green'
                            isChecked={sites[site]}
                            onChange={(event) => {
                                setSites((prev) => {
                                    return { ...prev, [site]: event.target.checked }
                                })
                            }}
                        >
                            {site}
                        </Checkbox>)
                    })
                }

            </Stack>

        </>
    )
}
export default SiteFilter;
