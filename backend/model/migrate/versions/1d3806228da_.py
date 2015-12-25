"""Increase field name in customer

Revision ID: 1d3806228da
Revises: 4ac191f72d8
Create Date: 2015-07-31 16:03:34.137347

"""

# revision identifiers, used by Alembic.
revision = '1d3806228da'
down_revision = '4ac191f72d8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customer', 'name',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=256),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customer', 'name',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=True)
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

