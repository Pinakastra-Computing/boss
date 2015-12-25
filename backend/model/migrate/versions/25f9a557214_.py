"""Rename fitter tables

Revision ID: 25f9a557214
Revises: 388ee1949b1
Create Date: 2015-07-03 15:19:53.075790

"""

# revision identifiers, used by Alembic.
revision = '25f9a557214'
down_revision = '388ee1949b1'
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
    op.create_table('tenant',
    sa.Column('tenant_id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('last_collected', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('tenant_id')
    )
    op.create_table('sales_order',
    sa.Column('sale_order_id', sa.Integer(), nullable=False),
    sa.Column('tenant_id', sa.String(length=100), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenant.tenant_id'], ),
    sa.PrimaryKeyConstraint('sale_order_id', 'tenant_id', 'start', 'end')
    )
    op.create_table('service_usage',
    sa.Column('tenant_id', sa.String(length=100), nullable=False),
    sa.Column('service_id', sa.String(length=100), nullable=False),
    sa.Column('time_label', sa.String(length=10), nullable=False),
    sa.Column('service_name', sa.Text(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('cost', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenant.tenant_id'], ),
    sa.PrimaryKeyConstraint('tenant_id', 'service_id')
    )
    op.create_index(op.f('ix_service_usage_time_label'), 'service_usage', ['time_label'], unique=False)
    op.drop_table('fitter_last_run')
    op.drop_table('fitter_usage_entry')
    op.drop_table('fitter_resources')
    op.drop_table('fitter_sales_orders')
    op.drop_table('fitter_tenants')
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fitter_usage_entry',
    sa.Column('service', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('unit', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('volume', mysql.DECIMAL(precision=20, scale=2), nullable=False),
    sa.Column('resource_id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('tenant_id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('start', mysql.DATETIME(), nullable=False),
    sa.Column('end', mysql.DATETIME(), nullable=False),
    sa.Column('created', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['resource_id', 'tenant_id'], ['fitter_resources.id', 'fitter_resources.tenant_id'], name='fk_resource_constraint'),
    sa.PrimaryKeyConstraint('service', 'resource_id', 'tenant_id', 'start', 'end'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('fitter_sales_orders',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('tenant_id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('start', mysql.DATETIME(), nullable=False),
    sa.Column('end', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['tenant_id'], ['fitter_tenants.id'], name='fitter_sales_orders_ibfk_1'),
    sa.PrimaryKeyConstraint('id', 'tenant_id', 'start', 'end'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('fitter_resources',
    sa.Column('id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('tenant_id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('info', mysql.TEXT(), nullable=True),
    sa.Column('created', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['tenant_id'], ['fitter_tenants.id'], name='fitter_resources_ibfk_1'),
    sa.PrimaryKeyConstraint('id', 'tenant_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('fitter_tenants',
    sa.Column('id', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('name', mysql.TEXT(), nullable=False),
    sa.Column('info', mysql.TEXT(), nullable=True),
    sa.Column('created', mysql.DATETIME(), nullable=False),
    sa.Column('last_collected', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('fitter_last_run',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('last_run', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_service_usage_time_label'), table_name='service_usage')
    op.drop_table('service_usage')
    op.drop_table('sales_order')
    op.drop_table('tenant')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

