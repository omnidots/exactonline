# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Combines the helper superclasses and the helper resource managers into the
ExactApi class.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015-2021 Walter Doekes, OSSO B.V.
"""
from ..rawapi import ExactRawApi

from .autorefresh import Autorefresh
from .unwrap import Unwrap
from .v1division import V1Division

from .accounts import Accounts
from .bankaccounts import BankAccounts
from .bulksalesitemprices import BulkSalesItemPrices
from .contacts import Contacts
from .documentattachments import DocumentAttachments
from .documents import Documents
from .goodsdeliveries import GoodsDeliveries
from .invoices import Invoices
from .items import Items
from .ledgeraccounts import LedgerAccounts
from .plannedsalesreturns import PlannedSalesReturns
from .quotations import Quotations
from .receivables import Receivables
from .relations import Relations
from .stockserialnumbers import StockSerialNumbers
from .transactionlines import TransactionLines
from .salespricelistperiods import SalesPriceListPeriods
from .salespricelists import SalesPriceLists
from .salespricelistvolumediscounts import SalesPriceListVolumeDiscounts
from .supplieritems import SupplierItems
from .syncsalesitemprices import SyncSalesItemPrices
from .vatcodes import VatCodes


class ExactApi(
    # Talk to /api/v1/{division} directly.
    V1Division,
    # Strip the surrounding "d" and "results" dictionary
    # items.
    Unwrap,
    # Ensure that tokens are refreshed in a timely manner.
    Autorefresh,
    # The base class comes last: talk to /api.
    ExactRawApi
):
    accounts = Accounts.as_property()
    bankaccounts = BankAccounts.as_property()
    bulksalesitemprices = BulkSalesItemPrices.as_property()
    contacts = Contacts.as_property()
    documentattachments = DocumentAttachments.as_property()
    documents = Documents.as_property()
    goodsdeliveries = GoodsDeliveries.as_property()
    invoices = Invoices.as_property()
    items = Items.as_property()
    ledgeraccounts = LedgerAccounts.as_property()
    plannedsalesreturns = PlannedSalesReturns.as_property()
    quotations = Quotations.as_property()
    receivables = Receivables.as_property()
    relations = Relations.as_property()
    stockserialnumbers = StockSerialNumbers.as_property()
    transactionlines = TransactionLines.as_property()
    salespricelists = SalesPriceLists.as_property()
    salespricelistvolumediscounts = SalesPriceListVolumeDiscounts.as_property()
    salespricelistperiods = SalesPriceListPeriods.as_property()
    supplieritems = SupplierItems.as_property()
    syncsalesitemprices = SyncSalesItemPrices.as_property()
    vatcodes = VatCodes.as_property()
