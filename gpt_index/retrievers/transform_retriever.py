from typing import List, Optional
from gpt_index.data_structs.node_v2 import NodeWithScore
from gpt_index.indices.base_retriever import BaseRetriever
from gpt_index.indices.query.query_transform.base import BaseQueryTransform
from gpt_index.indices.query.schema import QueryBundle


class TransformRetriever(BaseRetriever):
    """Transform Retriever.

    Takes in an existing retriever and a query transform and runs the query transform
    before running the retriever.

    """

    def __init__(
        self,
        retriever: BaseRetriever,
        query_transform: BaseQueryTransform,
        transform_extra_info: Optional[dict] = None,
    ) -> None:
        self._retriever = retriever
        self._query_transform = query_transform
        self._transform_extra_info = transform_extra_info

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        query_bundle = self._query_transform.run(
            query_bundle, extra_info=self._transform_extra_info
        )
        return self._retriever.retrieve(query_bundle)
