#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "hiredis.h"

#define CHECK(X) if ( !X || X->type == REDIS_REPLY_ERROR ) { printf("Error\n"); exit(-1); }

redisContext *redis_conn(const char *ip, int port)
{
    redisContext *ctx = NULL;
    ctx = redisConnect(ip, port);
    if (!ctx)
    {
        printf("Could not connect to redis-server, exiting ...\n");
        exit(-1);
    }
    return ctx;
}

redisContext *redis_conn_timeout(const char *ip, int port, 
        struct timeval timeout)
{
    redisContext *ctx = NULL;
    ctx = redisConnectWithTimeout(ip, port, timeout);
    if (!ctx || ctx->err)
    {
        printf("Could not connect to redis-server, exiting ... %s\n", ctx->errstr);
        exit(-1);
    }
    return ctx;
}

int set_string_key(redisContext *ctx, const char *key, const char *value)
{
    redisReply *reply = NULL;
    char cmd[1024];
    int ret = 1;
    snprintf(cmd, 1024, "SET %s %s", key, value);
    reply = (redisReply *) redisCommand(ctx, cmd);
    //reply = (redisReply *) redisCommand(ctx, "SET %s %s", key, value);
    if (reply->type == REDIS_REPLY_ERROR)
    {
        ret = 0;
    }
    freeReplyObject(reply);
    return ret;
}

void incr_string_val(redisContext *ctx, const char *key, int incr)
{
    redisReply *reply = NULL;
    char cmd[1024];
    if (incr <= 0)
    {
        printf("Nothing to be done, correct your increment value\n");
        return;
    }
    else if (incr == 1)
    {
        snprintf(cmd, 1024, "INCR %s", key);
    }
    else
    {
        snprintf(cmd, 1024, "INCRBY %s %d", key, incr);
    }
    reply = (redisReply *) redisCommand(ctx, cmd);
    if (reply->type == REDIS_REPLY_ERROR)
    {
        printf("Could not execute %s\n", cmd);
    }
    freeReplyObject(reply);
    return;
}

void set_string_key_expire(redisContext *ctx, const char *key, int expiry)
{
    redisReply *reply = NULL;
    reply = (redisReply *) redisCommand(ctx, "EXPIRE %s %d", key, expiry);
    if (reply->type == REDIS_REPLY_ERROR)
    {
        printf("Could not set expiry\n");
    }
    freeReplyObject(reply);
}

void set_string_key_expire_ms(redisContext *ctx, const char *key, int expiry)
{
    redisReply *reply = NULL;
    reply = (redisReply *) redisCommand(ctx, "PEXPIRE %s %d", key, expiry);
    if (reply->type == REDIS_REPLY_ERROR)
    {
        printf("Could not set expiry\n");
    }
    freeReplyObject(reply);
}


void get_string_val(redisContext *ctx, const char *key, char *value, int value_len)
{
    redisReply *reply = NULL;
    char cmd[1024];

    snprintf(cmd, 1024, "GET %s", key);

    reply = (redisReply *) redisCommand(ctx, cmd);
    if (reply->type != REDIS_REPLY_ERROR)
    {
        snprintf(value, value_len, "%s", reply->str);
    }
    freeReplyObject(reply);
}

void string_example(redisContext *ctx)
{
    int ret_val = set_string_key(ctx, "BOO", "1");
    if (ret_val == REDIS_REPLY_ERROR)
    {
        printf("redis returned error for the command\n");
    }
    else
    {
        printf("redis reply: %d\n", ret_val);
    }

    //will use incr call
    incr_string_val(ctx, "BOO", 1);
    //value should be 2
    char value[1024];
    get_string_val(ctx, "BOO", value, 1024);
    printf("value_len :%s\n", value);
    memset((void *)value, 0, 1024);
    //will use incrby call
    incr_string_val(ctx, "BOO", 5);
    //value should be 7
    get_string_val(ctx, "BOO", value, 1024);
    printf("value_len :%s\n", value);
    
    //SETS EXPIRY for a key in seconds
    set_string_key_expire(ctx, "BOO", 10);
    
    ret_val = set_string_key(ctx, "DOO", "1");
    //SETS EXPIRY for a key in milliseconds
    set_string_key_expire_ms(ctx, "DOO", 10000);
}

int main()
{
    int ret_val = 0; 

    struct timeval t = {1, 500000};

    //Create redisContext without timeout
    //redisContext *ctx = redis_conn(", 6379);

    //Create redisContext with timeout
    redisContext *ctx = redis_conn_timeout("localhost", 6379, t);

    //Following is an example of STRING data-type
    string_example(ctx);
    printf("IIIII 2\n");
    redisFree(ctx);
}
